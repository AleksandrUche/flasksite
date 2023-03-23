from flask import Flask, render_template
app = Flask(__name__)

menu = ["Установка", "Первое приложение", "Обратная связь"]


@app.route('/')
def index():
    return render_template('index.html', title='Главная страница', menu=menu)


@app.route("/about")
def about():
    return render_template('about.html', title='О сайте', content='Про Flask')


if __name__ == "__main__":
    app.run(debug=True)
