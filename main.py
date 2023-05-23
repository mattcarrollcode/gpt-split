import os

import flask
import sentry_sdk
import tiktoken
from flask import Flask, render_template
from sentry_sdk import set_context, set_tag
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="https://3f028c12bf974d988f2a41d3e8929ec8@o4505190542540800.ingest.sentry.io/4505190543851520",
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0,
)

if (
    "RAILWAY_ENVIRONMENT" in os.environ
    and os.environ["RAILWAY_ENVIRONMENT"] == "production"
):
    set_tag("environment", "prod")

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello():
    request = flask.request
    if request.method == "GET":
        models = list(tiktoken.model.MODEL_TO_ENCODING.keys())
        with open("a-study-in-scarlet.txt") as file:
            example_text = file.read()
        return render_template("index.html", models=models, example_text=example_text)

    model = request.form["model"]
    tokenlimit = request.form["tokenlimit"]
    text = request.form["text"]
    enc = tiktoken.encoding_for_model(model)
    chunks = split_on_n_tokens(text, int(tokenlimit), enc)

    set_context(
        "split_request",
        {
            "model": model,
            "token_limit": tokenlimit,
            "text_length": len(text),
            "num_chunks": len(chunks),
        },
    )
    return render_template("results.html", chunks=chunks)


def split_on_n_tokens(text: str, n: int, enc: tiktoken.Encoding) -> list[str]:
    list_of_str = []
    enc_text = enc.encode(text)
    index = 0
    if n > len(enc_text):
        return [text]

    while index < len(enc_text):
        prev_index = index
        index += n

        enc_text_chunk = enc_text[prev_index:index]
        text_chunk = enc.decode(enc_text_chunk).strip()
        list_of_str.append(text_chunk)
    return list_of_str


if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT", default=5000))
