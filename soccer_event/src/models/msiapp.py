from flask import render_template
from __init__ import app
from train_model import Track


# Create view into index page that uses data queried from Track database
# and inserts it into the msiapp/templates/index.html template
@app.route('/')
def index():
    return render_template('index.html', tracks=Track.query.all())


if __name__ == "__main__":
    app.run(debug=True)