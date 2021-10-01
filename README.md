### 10.05_Sentry </br>
#### Задание 1: </br>
Получить Centry Free cloud account на sentry.io. Пришлите скриншот меню Projects: </br>
![Sentry_project](https://github.com/murzinvit/screen/blob/769e3bdaf33b56111059a86a9600074bd8df2b95/Sentry_project.jpg) </br>
#### Задание 2: </br>
Создайте python проект и нажмите Generate sample event для генерации тестового события </br>
Для выполнения задание предоставьте скриншот Stack trace из этого события и список событий проекта, после нажатия Resolved </br>
Python скрипт для теста sentry: [test_app.py](https://github.com/murzinvit/10.05_Sentry/blob/135f53e99bb1f29ff6e29b05f4a048aedf18cfae/py_project/test_app.py) </br>
Для установки sentry-sdk на Debian 9 инструкции - pip install --upgrade sentry-sdk оказалось недостаточно. </br> 
В python скрипте инструкция - `import sentry-sdk` выдавала - ModuleNotFound </br>
Исправление: `pip install sentry`, `apt-get install python3-pip`, `pip3 install --upgrade sentry`, `pip install --upgrade sentry` </br>
Cкриншот Stack trace из тестового события: </br>
![Sentry_stack_trace](https://github.com/murzinvit/screen/blob/eb44556374aedda99f79af5103d282a45dbce100/Sentry_stack_trace.jpg) </br>
Cкриншот после нажатия Resolved: </br>
![Sentry_after_sample_error](https://github.com/murzinvit/screen/blob/f20eec07acd6a835ec78e682bd5a522b6393303d/Sentry_after_sample_error.jpg) </br>

#### Задание 3: </br>
Снова сгенерируйте событие Generate sample event. Выберите проект и создайте дефолтное правило алёртинга, без настройки полей </br>

#### Задание повышенной сложности: </br>

