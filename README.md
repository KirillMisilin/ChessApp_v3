Шахматное приложение.
Лучше клонировать ветку develop, так как там есть БД, так что ее не придется настраивать для правильной работы приложения.
Использование:
  1. Склонировать ветку develop.
  2. Перейти в проект, установить зависимости:
     pip install -r requirements.txt
  3. Запустить файл manage.py:
     manage.py runserver
  Для игры необходимо зарегистрироваться (логин и пароль).
  После нажать "Find game", это поставит Вас в очередь для игры, пока другой пользователь не начнет тоже искать игру. Можно открыть второе окно и потестить.
  Повторное нажатие запустит игру сам с собой.
Описание:
  Бэкенд на django + channels и redis для работы с веб-сокетами. Еще не доделан, так что могут вылезать ошибки, но базовый функционал есть. Фронтэнд еще не доделан, так что внешний вид так себе.