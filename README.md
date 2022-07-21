# Flask Web

Flask web application boilerplate

## Docker
```
docker build -t web .
docker run -d -p 80:5000 --name web web

docker stop web
docker rm web
docker image rm web
```
