import sys
import pathlib
from langchain.document_loaders import DirectoryLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI

from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import DocArrayInMemorySearch


from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage


DOCS_PATH = f"{pathlib.Path(__file__).parent.resolve()}/documents"
RELEVANCY_CUTOFF = 0.75

loader = DirectoryLoader(DOCS_PATH, glob="**/*.*", show_progress=True)
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=2500, chunk_overlap=20)
docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()
db = DocArrayInMemorySearch.from_documents(docs, embeddings)


def get_contextual_answers(query):
    docs = db.similarity_search_with_score(query)

    relevant_chunks = []
    relevant_documents = []
    for doc in docs:
        if doc[1] > RELEVANCY_CUTOFF:
            relevant_chunks.append(doc)
            source_file = doc[0].metadata["source"]
            if source_file not in relevant_documents:
                relevant_documents.append(source_file)

    supplemental_context = "\n\n\n".join(
        [doc[0].page_content for doc in relevant_chunks]
    )

    chat = ChatOpenAI(temperature=0)
    messages = [
        [
            SystemMessage(
                content=f"You are a helpful assistant that is aware of the following information:\n\n\n{supplemental_context}"
            ),
            HumanMessage(content=query),
        ]
    ]

    result = chat.generate(messages)
    return result.generations[0][0].text, relevant_chunks, relevant_documents


def main(args):
    query = None
    print(
        """👩‍⚕️ > Welcome to DocBot, your friendly neighborhood embeddings retrieval chatbot!
     Ask me any question you'd pose to ChatGPT and I'll make sure any relevant info you've
     placed in my ./documents folder is incorporated in forming the response.
"""
    )
    while query != "q":
        query = input("👩‍⚕️ > ")
        if query == "q":
            exit("👋 Thanks for using DocBot!")
        response, chunks, docs = get_contextual_answers(query)
        if len(docs) < 1:
            print("⚠️ Found no sufficiently related documents")
        else:
            found_files = "\n   -".join(docs)
            print(
                f"🟢 Located {len(chunks)} relevant chunks in {len(docs)} document(s): \n   -{found_files}"
            )
        print(f"✅ > {response}")


if __name__ == "__main__":
    main(sys.argv)
