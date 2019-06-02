# nc99.co
Website for the nc99 Minecraft Server

## Running
To create the database for the first time, run
```bash
python manage.py migrate
python manage.py createsuperuser
```

Then you can build a Docker container and use it:

```bash
docker build -t nc99.co .
docker run -d -v /path/to/db.sqlite3:/nc99.co/nc99/db.sqlite3 -p 8000:8000 nc99.co
```

To get static content working, set up a reverse proxy and route `/static` to `nc99/static/`.
