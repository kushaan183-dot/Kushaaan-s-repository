from flask import Flask, render_template, request

app = Flask(__name__)


def count_vowels(s: str) -> int:
    """Return the number of vowels in the given string (case-insensitive)."""
    return sum(1 for c in s.lower() if c in "aeiou")


@app.route('/', methods=['GET', 'POST'])
def index():
    text = ''
    count = None
    if request.method == 'POST':
        text = request.form.get('text', '')
        count = count_vowels(text)
    return render_template('index.html', text=text, count=count)


if __name__ == '__main__':
    app.run(debug=True)
