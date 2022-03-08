docker build -t my_app:prod -f config/prod/Dockerfile .
docker run --publish 8000:8000 --name my_app_prod my_app:prod