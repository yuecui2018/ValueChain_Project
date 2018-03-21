from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# flask application
application = Flask(__name__)

# config
application.config.from_pyfile('config.py', silent = True)

# Initialize the database
db = SQLAlchemy(application)

class Soccer(db.Model):
	index = db.Column(db.Integer, primary_key = True)
	time = db.Column(db.Integer, nullable = False)
	side_val = db.Column(db.String(20), nullable = False)
	event_val = db.Column(db.String(20), nullable = False)
	assist_val = db.Column(db.String(20), nullable = False)
	fastbreak_val = db.Column(db.String(20), nullable = False)

	def __repr__(self):
		return '<URL %r>' % self.url