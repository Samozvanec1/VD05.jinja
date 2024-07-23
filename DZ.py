from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def render_one():
    return render_template('DZhome.html')

@app.route('/ёжики')
def render_two():
    return render_template('DZabout.html')

if __name__ == '__main__':
    app.run()