from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def render_two():
    context ={
        "caption": "Привет мир! Всем пока!",
        "count": 8,
        "users": ["Иван", "Петр", "Сидор", "Вася", "Коля"],
        "poem":["Не криви улыбку, руки теребя,-",
        "Я люблю другую, только не тебя.",

        "Ты сама ведь знаешь, знаешь хорошо —",
        "Не тебя я вижу, не к тебе пришел.",

        "Проходил я мимо, сердцу все равно —",
        "Просто захотелось заглянуть в окно."],

    }
    return render_template('shablon.html', **context)

if __name__ == '__main__':
    app.run()