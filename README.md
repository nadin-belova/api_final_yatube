
#  Проект «API для Yatube»
## Описание(что это за проект, какую задачу он решает, в чём его польза)
    Проект api_yatube - это API социальной сети yatube.

    С помощью api_yatube можно запрашивать данные о постах, группах, комментариях в социальной сети Yatube,
    а также создавать новые посты и комментарии ,изменять существущие посты и коментарии при наличии прав доступа .

    Yatube - это учебный проект курса "backend-python" от Яндекс-Практикума.
    
    
 ## Установка. Как развернуть проект на локальной машине
    Клонировать репозиторий и перейти в него в командной строке:

    ```git clone git@github.com:nadin-belova/api_final_yatube.git```

    ```cd api_final_yatube```

Cоздать и активировать виртуальное окружение:

python3 -m venv venv

source venv/bin/activate

Установить зависимости из файла requirements.txt:

python3 -m pip install --upgrade pip

pip install -r requirements.txt

Выполнить миграции:

python3 manage.py migrate

Запустить проект:

python3 manage.py runserver

    
    
 ##  Примеры. Некоторые примеры запросов к API.
