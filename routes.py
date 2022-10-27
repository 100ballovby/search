from app import app
from datetime import datetime
from flask import redirect, render_template, request   # тут реквесты фласка
import requests as r  # тут реквесты для сбора данных


@app.route('/')
def index():
    return render_template('index.html',
                           current_time=datetime.utcnow())


@app.route('/github-search', methods=['GET', 'POST'])
def git_search():
    if request.method == 'POST':
        lang = request.form.get('lang')
        sort = request.form.get('sort')

        url = 'https://api.github.com/search/repositories'  # ссылка для подключения к API GitHub
        params = {
            'q': f'language:{lang}',
            'sort': f'sort={sort}'
        }  # параметры запроса
        resp = r.get(url, params=params)  # обращаюсь к API и отдаю нужный запрос
        resp_json = resp.json()  # превращаю ответ сервера GitHub в итерируемый объект, который можно открыть в шаблоне
        result = resp_json['items']  # получаю все найденные репозитории по ключу items
        print(result)
        return render_template('github.html', repos=result)  # вывожу страницу и передаю репозитории как аргумент
    return render_template('github.html')