from datetime import datetime, timedelta
from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.models import Stats
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
def index():
    oldest_recent = datetime.utcnow() - timedelta(minutes=1)
    recent_air_stats = Stats.query.filter(Stats.timestamp >= oldest_recent).order_by(Stats.timestamp).all()
    return render_template('data.html', stats=recent_air_stats, since=oldest_recent)
