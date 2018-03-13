from msiapp import db
from msiapp.models import Track


"""Ingestion module
This module is meant to be called to ingest data and place it into db. Once an API is used
the module can be extended with a function that calls the API and puts the data into the db.
Functionality presumes that the db has already been created. 
"""

def seed_db():
    """Seed a preexisting db with dat
    Returns:
    """
    track1 = Track(time='90', side='Away', fast_break='yes')
    track2 = Track(time='1', side='Away', fast_break='no')
    db.session.add(track1)
    db.session.add(track2)
    db.session.commit()


if __name__ == "__main__":
    seed_db()