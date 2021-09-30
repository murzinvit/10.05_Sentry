### 10.05_Sentry </br>
#### Задание 1: </br>
Получить Centry Free cloud account на sentry.io. Пришлите скриншот меню Projects: </br>
![Sentry_project](https://github.com/murzinvit/screen/blob/769e3bdaf33b56111059a86a9600074bd8df2b95/Sentry_project.jpg) </br>
#### Задание 2: </br>
Создайте python проект и нажмите Generate sample event для генерации тестового события </br>
Для выполнения задание предоставьте скриншот Stack trace из этого события и список событий проекта, после нажатия Resolved </br>
Python скрипт для теста sentry: [test_app.py](https://github.com/murzinvit/10.05_Sentry/blob/135f53e99bb1f29ff6e29b05f4a048aedf18cfae/py_project/test_app.py) </br>
Для установки sentry-sdk на Debian 9 инструкции - pip install --upgrade sentry-sdk оказалось не достаточно. import sentry-sdk не работало </br>
Потребовалось поставить pip3 - apt-get install python3-pip, и pip3 install --upgrade sentry </br>

#### Задание 3: </br>
Снова сгенерируйте событие Generate sample event. Выберите проект и создайте дефолтное правило алёртинга, без настройки полей </br>

#### Задание повышенной сложности: </br>
