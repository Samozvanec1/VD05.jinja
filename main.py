from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def render_one():
    context ={
        "caption": "Привет мир! Всем привет!",
        "link": "/test2"
    }
    return render_template('index.html', **context)
@app.route('/test2')
def render_two():
    context ={
        "caption": "Привет мир! Всем пока!",
        "link": "/"
    }
    return render_template('index.html', **context)

if __name__ == '__main__':
    app.run()