from schema import db
from schema import Soccer
from config import SQLALCHEMY_DATABASE_URI

def create_db():
	db.drop_all()
	db.create_all()
	track1 = Soccer(index=1, time=20, side_val='Home',event_val = 'Attempt',assist_val = 'Yes',fastbreak_val = 'No')
	db.session.add(track1)
	db.session.commit()

if __name__ == "__main__":
	create_db()