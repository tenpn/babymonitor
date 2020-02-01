"""the entry point for the app"""
import threading
import temp
from app import app, db
from app.models import Stats

@app.shell_context_processor
def make_shell_context():
    """remember to add new db tables!"""
    return {'db': db, 'Stats': Stats}

threading.Thread(target=temp.temp_deamon).start()
