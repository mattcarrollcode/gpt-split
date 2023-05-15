from flask import Flask
import tiktoken

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    if flask.request.method == 'GET':
        return render_template("index.html")
    
    model = request.form['model']
    tokenlimit = request.form['tokenlimit']
    text = request.form['text']
    # enc = tiktoken.get_encoding("cl100k_base")
    # assert enc.decode(enc.encode("hello world")) == "hello world"

    # To get the tokeniser corresponding to a specific model in the OpenAI API:
    enc = tiktoken.encoding_for_model("gpt-4")
    enc.encode(text)
    return enc



