server:
1-server > create .env file

SECRET_KEY=
DEBUG=
ENV_NAME=
SQL_DATABASE=
SQL_USER=
SQL_PASSWORD=
SQL_HOST=
SQL_PORT=

2-python -m venv env
3-env/Scripts/Activate
4-pip install -r requirements.txt
5-python manage.py migrate
6-python manage.py runserver

client:
1-npm install
2-npm start
