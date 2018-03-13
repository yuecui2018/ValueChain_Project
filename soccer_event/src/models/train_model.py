from __init__ import db


# Create a data model for the database to be setup for the app
class Track(db.Model):
    time = db.Column(db.Integer, primary_key=True)
    side = db.Column(db.String(100), unique=False, nullable=False)
    fast_break = db.Column(db.String(100), unique=False, nullable=False)

    def __repr__(self):
        return '<Track %r>' % self.title