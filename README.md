#Install and Run with docker-compose
```
cp .env.example .env
```
Put your postgres settings to .env file
```
docker-compose run app bash -c "python manage.py makemigrations && python manage.py migrate"
docker-compose up --build
```
