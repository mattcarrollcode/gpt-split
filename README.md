# GPT Split

This web app splits up large blocks of text on a set number of tokens as defined by OpenAI for better ingestion into tools like ChatGPT. You can see a live demo here: <a href="https://gpt-split-production.up.railway.app/" target="_blank">https://gpt-split-production.up.railway.app/</a>.

![GPT split demo screenshots](https://raw.githubusercontent.com/mattcarrollcode/gpt-split/main/screenshot-demo.png)

Note: This has only been tested to work on macOS and [Railway](https://railway.app/)

## Setup

1. Clone this repo and `cd` to the root of the repo
1. Install pyenv and pyenv-virtualenv: `brew install pyenv pyenv-virtualenv`
1. Add the following to your `~/.bashrc` or `~/.zshrc` file:
   ```
   export PYENV_ROOT="$HOME/.pyenv"
   export PATH="$PYENV_ROOT/bin:$PATH"
   eval "$(pyenv init -)"
   eval "$(pyenv virtualenv-init -)"
   ```
1. Install Python version 3.11.1: `pyenv install 3.11.1`
1. Create a new Python 3.11.1 virtualenv called `gpt-split`: `pyenv virtualenv 3.11.1 gpt-split`
1. Configure pyenv to use the `gpt-split` virtualenv in the repo: `pyenv local gpt-split`
1. Install requirements: `pip install -r requirements.txt`

## Run

* To run the app in dev mode, run: `python main.py`
* To run the app in prod mode, run: `gunicorn main:app`
* To run the unit tests, run: `python -m unittest`

## Next steps
* Fix Sentry message capture in `templates/results.html`
* Input validation
* Style the UI
* Better mobile support
* Debug mobile copy-paste support
* Support other tokenziers besides tiktoken
* Prompt suggestions to help LLMs ingest multiple messages together
