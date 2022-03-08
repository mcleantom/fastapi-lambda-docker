docker build -t my_app:dev -f config/dev/Dockerfile .
docker run -d --publish 8000:8000 --name my_app_dev 