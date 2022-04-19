#**Setting postgres**
```
cp .env.example .env
```
___Put your postgres settings to .env file___



#**Run with docker-compose**
```
docker-compose run app bash -c "python manage.py makemigrations && python manage.py migrate"
docker-compose up --build
```
