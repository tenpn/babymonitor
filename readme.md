# flask

https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

```
> python3 -m venv venv
> source venv/bin/activate
> pip install -r requirements.txt
> flask run --host=0.0.0.0
```

db:

```
> flask db init # one time 
> flask db migrate -m "msg"
> flask db upgrade
```

to update requirements.txt: 
`pip freeze > requirements.txt`

# deployment

https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xvii-deployment-on-linux

``` 
> sudo apt-get install supervisor
> sudo cp superdbabymon.conf /etc/supervisor/conf.d/
> pip install gunicorn
> sudo supervisorctl reload
```

