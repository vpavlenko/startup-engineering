Подготовка к занятию
--------------------

Зарегистрируйтесь на [aws.amazon.com](http://aws.amazon.com/). Возьмите [инструкцию](https://spark-public.s3.amazonaws.com/startup/lecture_slides/lecture2-interactive-start.pdf) с курса Startup Engineering на Курсере. По той же инструкции поставьте Cygwin, если у вас Виндоус. Вам нужен только продукт EC2, вам надо создать только один инстанс t1.micro (он бесплатен первый год). Советую ставить на него Ubuntu Server 13.10.

План занятия
------------

1. Протоколы TCP, IP, HTTP
    - [Что происходит при загрузке страницы](http://friendlybit.com/css/rendering-a-web-page-step-by-step/)
    - [Простой HTTP-сервер на Питоне](https://github.com/vpavlenko/reinhardt)

2. Джанго: urls/views/templates, наследование в шаблонах, настройка админского интерфейса
    - [Простой проект на Джанго.](https://github.com/vpavlenko/django-lectures)
        Скачайте и запустите у себя guestbook. Затем создайте свой проект и
        сделайте первые два пункта в задании про вики-движок (на 40 баллов).
    - [Проект посложнее.](https://github.com/vpavlenko/zpshch) Усложните функционал до появления
        моделей с внешними ключами, сделайте наследование в шаблонах, настройте админку.
    - [Серьёзный проект.](https://github.com/vpavlenko/pythontutor-ru) Но с ужасным кодом. Захотите помочь в разработке - пишите.

3. [virtualenv, деплоймент на Heroku](heroku)

4. [Деплоймент на Амазон: shell, nginx, uwsgi](amazon)

3. [Безопасность: HTTPS, соленые и перченые хеши, clickjacking и CSRF](http://tech.yandex.ru/education/shri/msk-2012/talks/540/)
