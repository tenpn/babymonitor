# flask

https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

```
> python3 -m venv venv
> source venv/bin/activate
> pip install flask python-dotenv flask-wtf flask-sqlalchemy flask-migrate flask-login RTIMULib sense-hat picamera
> flask run --host=0.0.0.0
```

db:

```
> flask db init # one time 
> flask db migrate -m "msg"
> flask db upgrade
```
