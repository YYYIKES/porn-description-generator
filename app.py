from flask import Flask, render_template, url_for, request
import markovify


app = Flask(__name__)

with open('static/datasets/xhamster-descriptions-scrubbed.txt') as f:
    text = f.read()

text_model = markovify.Text(
    text, state_size=3, well_formed=False)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        for i in range(1):
            statement = text_model.make_short_sentence(500)
        return render_template('index.html', statement=statement)
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
