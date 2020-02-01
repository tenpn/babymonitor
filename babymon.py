from app import app, db
from app.models import Stats
import temp
import threading

@app.shell_context_processor
def make_shell_context():
    return { 'db': db, 'Stats': Stats }

threading.Thread(target=temp.temp_deamon).start()
