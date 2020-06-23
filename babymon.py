"""the entry point for the app"""
import threading
from werkzeug.serving import is_running_from_reloader
from app.models import Stats
from app import app, db
import temp

@app.shell_context_processor
def make_shell_context():
    """remember to add new db tables!"""
    return {'db': db, 'Stats': Stats}

if not is_running_from_reloader():
    threading.Thread(target=temp.temp_record_deamon).start()
    threading.Thread(target=temp.temp_cleanup_deamon).start()
