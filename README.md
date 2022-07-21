# Flask Web

Flask web application boilerplate

## Development

1. Set environment variables

```
FLASK_APP=web.app
FLASK_DEBUG=1
FLASK_ENV=development
FLASK_RUN_HOST=localhost
FLASK_RUN_PORT=80
DATABASE_URL=db.sqlite3
SECRET_KEY=secret
```

1. Initialize database

```
flask db migrate
flask db upgrade
```

1. Run dev server

```
flask run
```

## PyCharm Configuration

![PyCharmConfiguration](https://i.imgur.com/A7d18Is.png)

## Docker
```
docker build -t web .
docker run -d -p 80:5000 --name web web

docker stop web
docker rm web
docker image rm web
```
