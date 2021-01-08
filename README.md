# geekshop_final

Созданный в процессе обучения интернет-магазин инструментов. 
Проект создан с использованием Django Framework, Postgre, 
bootstrap.

Для запуска на локальной машине:

1.  Клонируем репозиторий
    git clone https://github.com/nikolaeff80/geekshop-furniture
2.  Устанавливаем виртуальное окружение
    sudo pip install virtualenv
    Создаем окружение в папке проекта
    virtualenv venv
    Активируем его:

        source venv/bin/activate (для oc unix)

        \Путь до папки проекта\project\venv\Scripts\activate.bat (для oc windows)

3.  Устанавливаем зависимости
    pip install -r requirements.txt
4.  Выполняем миграции
    python manage.py makemigrations
    python manage.py migrate    


##  Cоздание начального пользователя для авторизации в django-admin
1.  Выполняем миграции
    python manage.py makemigrations
    python manage.py migrate 
2.  Создаем суперюзера 
    python manage.py createsuperuser
3.  Запускаем сервер 
    python manage.py runserver    
4.  Проверка юзера
    http://127.0.0.1:8000/admin/

