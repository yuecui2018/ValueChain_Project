from  __init__ import db
from train_model import Track


# Creates a table in the database provided as the 'SQLALCHEMY_DATABASE_URI'
# configuration parameter in __init__.py with the schema defined by models.Track()
def create_db():
    db.create_all()
    track1 = Track(time='20', side='Home', fast_break='yes')
    track2 = Track(time='45', side='Home', fast_break='no')
    db.session.add(track1)
    db.session.add(track2)
    db.session.commit()


if __name__ == "__main__":
    create_db()