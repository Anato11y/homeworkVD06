from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def form():
    user_data = None

    # Проверяем, была ли отправлена форма
    if request.method == 'POST':
        # Извлекаем данные из формы
        name = request.form.get('name')
        city = request.form.get('city')
        hobby = request.form.get('hobby')
        age = request.form.get('age')

        # Собираем данные в словарь для удобства передачи в шаблон
        user_data = {
            'name': name,
            'city': city,
            'hobby': hobby,
            'age': age
        }

    return render_template('form.html', user_data=user_data)


if __name__ == '__main__':
    app.run(debug=True)
