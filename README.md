# GPT Split

This web app splits up a large block of text on a set number of tokens for better ingestion into tools like ChatGPT

## Setup
1. Install Python
1. Install requirements: `pip install -r requirements.txt`

## Run

* App in dev mode: `python main.py`
* App in prod mode: `gunicorn main:app`
* Tests: `python -m unittest`

## Next steps
* Input validation
* Support other tokenziers besides tiktoken
* Style the UI
* Prompt suggestions for ingesting multiple message together
