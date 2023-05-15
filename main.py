from flask import Flask, render_template
import flask
import tiktoken
import os

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello():
    request = flask.request
    if request.method == 'GET':
        models = list(tiktoken.model.MODEL_TO_ENCODING.keys())
        print(models)
        return render_template("index.html", models=models)

    model = request.form['model']
    tokenlimit = request.form['tokenlimit']
    text = request.form['text']
    enc = tiktoken.encoding_for_model(model)
    chunks = split_on_n_tokens(text, int(tokenlimit), enc)
    return render_template("response-template.html", chunks=chunks)


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


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
