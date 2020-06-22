"""DB models
> flask db migrate -m "msg"
> flask db upgrade
"""
from datetime import datetime
from app import db

class Stats(db.Model):
    """One snapshot of the environment in the room"""
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    temp = db.Column(db.Float)

    def __repr__(self):
        return '<Stats {0:0.1f}dC @ {1}>'\
            .format(self.temp, self.timestamp.strftime("%m/%d/%y %H:%M.%S"))
