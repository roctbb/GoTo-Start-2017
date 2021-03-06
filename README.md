# GoTo-Start-2017

## Занятие 1: Синстаксис Python и работа с Pillow
1. Установка Anaconda (**Python 3.5** + набор библиотек, включая Pillow): https://www.continuum.io/downloads
2. Изучаем Python 3:
  - https://docs.python.org/3/tutorial/ - официальное руководство (на английском)
  - Марк Лутц. Изучаем Python, 4-е издание. - полноценный и подробный учебник
  - **http://pythontutor.ru/**
3. Работа с библиотекой Pillow (форк PIL - Python Image Library):
  - https://pillow.readthedocs.io/en/4.0.x/handbook/tutorial.html - документация
  - Цветовая обработка в Pillow - https://habrahabr.ru/post/163663/
  - Примеры c занятия - в папке lesson 1

**ДЗ: Фотофильтр на Python. 
Программа должна запрашивать путь к файлу, а затем на выбор предлагать несколько вариантов цветовой обработки фотографии, результат сохраняется в файл.** 

Постарайтесь подойти к задаче творчески и придумать собственный, уникальный фильтр. Сдать решение нужно на http://anytask.org.

Желательно просмотреть http://pythontutor.ru до седьмого урока включительно. Задачи прорешивать не обязательно.

## Занятия 2: Взаимодействие в внешними API
1. [Библиотека Requests - GET и POST запросы из Python](http://docs.python-requests.org/en/master/)
2. [microsoft cognitive services](https://www.microsoft.com/cognitive-services/en-us/apis)

**ДЗ: Фотофильтр, который использует распознавание лиц или зависит от настроения человека на фотографии.**

## Занятие 3: Обработка аудиоданных и использование PyAudio
1. Документация по PyAudio - https://people.csail.mit.edu/hubert/pyaudio/
2. Структура и содержимое wav файла (с кодом на СИ) - http://audiocoding.ru/article/2008/05/22/wav-file-structure.html
3. Еще про кодирование звука: [Википедия](https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D0%B4%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5_%D0%B7%D0%B2%D1%83%D0%BA%D0%BE%D0%B2%D0%BE%D0%B9_%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D0%B8)
4. Работа с микрофоном, динамиками, запись и обработка файлов + немного теории - в [примерах с комментариями](https://github.com/roctbb/GoTo-Start-2017/blob/master/Lesson%203/).

**ДЗ: 10 баллов: программа несколько секунд записывает звук и увеличивает частоту/накладывает музыку/переворачивает звук и воспроизводит его.**

**15 баллов: запись начинается когда пользователь начинает говорить и заканчивается, когда он замолкает. После воспроизведения процесс начинается сначала.**

## Занятие 4: Yandex SpeechKit

1. Документация по SpeechCloud - https://tech.yandex.ru/speechkit/

**ДЗ: Реализовать минипроект с использованием распознавания и синтеза речи.**

## Занятие 5: Соревнование ботов

1. Документация - https://roctbb.net
2. Тестирующая система - http://roctbb.net:8888

**ДЗ: Подготовиться к соревнованию.**


## Занятие 6: Telegram боты

1. Документация - https://core.telegram.org/bots/api
2. Небольшой учебник - https://groosha.gitbooks.io/telegram-bot-lessons/

**ДЗ: Бот для обработки фотографий или собственная идея.**

## Занятие 7: Веб-сервер Tornado

1. Общая схема работы по HTTP - [https://habrahabr.ru/post/215117/](https://habrahabr.ru/post/215117/).
2. Язык разметки HTML:
  - [самоучитель htmlbook.ru](http://htmlbook.ru/samhtml)
  - [Интерактивный курс по HTML/CSS](https://htmlacademy.ru/)
  - [HTML фреймфорк Bootstrap](http://getbootstrap.com)
3. Веб-сервер Tornado:
  - [Документация](http://www.tornadoweb.org/en/stable/)

**ДЗ: Написать сайт с тестом или случайной историей, которые зависят от введенных пользователем данных.**


