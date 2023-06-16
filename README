# DocBot

Your friendly neighborhood embeddings retrieval chatbot.

DocBot is a simple example of an in-memory embeddings retrieval chatbot which selectively adds relevant context to your GPT prompt for all documents placed in the `./documents` folder.

This project is a demo WIP and should not be considered feature complete - some aspects not presently covered include:

- Multi-message chat
- Configurable relevancy cutoff
- Command line arguments and piping

## Demo
![image](/demo.png)

## Setup
### Requirements
1. Provision an [OpenAI API key](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key) and set it as an environment variable named `OPENAI_API_KEY`

2. Activate the Python virtual environment:
```
source venv/bin/activate
```
3. Install requirements:
```
pip install -r requirements.txt
```

### `docbot` shortcut (optional)

If you cloned this repo in a folder other than `~/src` then update the path in the file `docbot` in the root of this repo.
	
i.e. if you cloned into `/code` you would update:
```~/src/docbot/venv/bin/python3 ~/src/docbot/main.py```

to be:

```/code/docbot/venv/bin/python3 /code/docbot/main.py```

Ensure that `docbot` has the appropriate file permissions for execution via `chmod +x docbot`

You can now invoke docbot via `docbot` and optionally add it to your PATH


## Usage

### Adding Documents
Any documents added to `./documents` or its subdirectories will be automatically indexed in memory upon execution.  New/edited documents added/edited while running will not be available until re-executed.

Any text based file (including markdown) is supported, although all files you'd like included in the index must have a file extension (e.g. `.txt` or `.md`)

### Running
If you followed the instructions to set up the `docbot` shortcut, simply run via `docbot`.

Otherwise, ensure the virtual environment is active and run via `python3 main.py`



Upon invoking `docbot` you'll be presented with a prompt and can provide any query you might ask ChatGPT - any documents with sufficient relevancy to your query will be included as context for the LLM to incorporate into its answer.
