from datetime import datetime, timedelta
from flask import render_template, flash, redirect, url_for, request, Response
from app import app, db
from app.models import Stats
from werkzeug.urls import url_parse
from camera.camera_pi import Camera

@app.route('/')
@app.route('/index')
def index():
    oldest_recent = datetime.utcnow() - timedelta(minutes=1)
    recent_air_stats = Stats.query.filter(Stats.timestamp >= oldest_recent).order_by(Stats.timestamp).all()
    return render_template('data.html', stats=recent_air_stats, since=oldest_recent)

def gen_video(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/cam')
def camera():
    return render_template('camera.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_video(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
