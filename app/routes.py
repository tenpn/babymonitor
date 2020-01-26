from flask import render_template, flash, redirect, url_for, request
from app import app
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
def index():
    return "Baby, monitor!"
