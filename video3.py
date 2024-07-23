from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def render_two():

    return render_template('video3.html')

if __name__ == '__main__':
    app.run()