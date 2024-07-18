# Пульт охраны банка

Это внутренний репозиторий для сотрудников банка «Сияние». Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, т.к. у вас нет доступа к БД, но можете свободно использовать код вёрстки или посмотреть как реализованы запросы к БД.

Пульт охраны - это сайт, который можно подключить к удалённой базе данных с визитами и карточками пропуска сотрудников нашего банка


## Как установить зависемости

Для установки этого проекта вам понадобится Python и Django, установленные на вашей компьютере. Затем вы можете клонировать этот репозиторий и установить необходимые зависимости с помощью:

Python должен быть уже установлен и его версия должна быть не младше 3.5.0. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirements.txt
```

## Передаём переменные окружения

Перед запуском программы, необходимо задать следующие переменные окружения в созданный вами :

- `DB_HOST`: Хост базы данных.
- `DB_PORT`: Порт, на котором работает ваша база данных.
- `DB_NAME`: Имя базы данных.
- `DB_USER`: Имя пользователя базы данных.
- `DB_PASSWORD`: Пароль пользователя базы данных.
- `SECRET_KEY`: Секретный ключ Django. Этот ключ используется для предоставления криптографической подписи и должен быть уникальным и сложным для угадывания.
- `DEBUG`: Режим отладки. Установлено значение `'True'`, чтобы включить режим отладки. Важно: не используйте режим отладки в продакшене!
- `ALLOWED_HOSTS`: Список хостов, которым разрешено обслуживать ваше Django-приложение. Хосты должны быть перечислены через запятую. Пример: `'localhost,127.0.0.1'`.

## Лицензия

Этот проект лицензирован по лицензии MIT License.

## Пример запука

Чтобы запустить этот проект, перейдите в каталог проекта и выполните следующую команду:

!`Пример выполнялся в командной строке перед этим открыв папку проекта`

```
python manage.py runserver 0.0.0.0:8000
```

Это запустит сервер разработки Django по адресу 0.0.0.0:8000. 

Чтобы получить доступ к веб-приложению, откройте браузер и введите следующий веб-адрес: http://127.0.0.1:8000/.

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.