Что установить заранее
======================

Установите Python3, setuptools и pip. При желании также установите текстовый редактор [Sublime Text](http://www.sublimetext.com/) и среду разработки [PyCharm](http://www.jetbrains.com/pycharm/).

Установка для Виндоус
---------------------

Устанавливаем [Python3](http://python.org/download/), [setuptools](http://www.lfd.uci.edu/~gohlke/pythonlibs/#setuptools)
и [pip](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pip).

Установка для Убунты
--------------------

	sudo apt-get install python3
    sudo apt-get install python3-setuptools
    sudo easy_install3 pip
    sudo pip-3.3 install django

Установка для Мака
------------------

	sudo port install python33
	# будет доступен в /opt/local/bin/python3.3
	sudo port install py33-pip
	# будет доступен в /opt/local/bin/pip-3.3


Базовые конструкции
===================

1. [Арифметика, списки, строки, множества, словари, if, for](python_examples.py)
2. [Словари, срезы](python_examples_2.py)
3. [min/max, функции, lambda](python_examples_3.py)
3. [Файловый ввод-вывод](http://contest.mccme.ru/pylernu/courses/1534/lessons/file_io/)

Как сдавать решения
-------------------

1. Залейте решение на [gist.github.com](https://gist.github.com/) или на [pastebin.com](http://pastebin.com/)
2. Вставьте ссылку в нужную графу в [Гуглодок с решениями](https://docs.google.com/spreadsheet/ccc?key=0AtJr69JHs0W0dHBtaExsZDR3TkpjaHphbTcwYmpLX3c&usp=sharing)

Зачем это нужно? Будем делать рефакторинг вашего кода.

Задачи
------

1. Пользователь вводит строку. Посчитайте количество различных слов в ней.
2. Пользователь вводит имя файла. Посчитайте, сколько раз в нём встречается каждое слово.

Темная магия
============

[Менеджеры контекста, генераторы, бесконечные последовательности](http://vpavlenko.github.io/startup-engineering/python/dark_magic/)