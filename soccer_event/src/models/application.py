from flask import render_template, request, redirect, url_for, flash
from __init__ import app, db
from train_model import Track


@app.route('/')
def index():
    """Main view that lists songs
    Create view into index page that uses data queried from Track database and
    inserts it into the msiapp/templates/index.html template
    :return: rendered html template
    """

    return render_template('index.html', tracks=Track.query.all())

@app.route('/add', methods=['POST'])
def add_entry():
    """View that process a POST with new song input
    :return: redirect to index page
    """

    track1 = Track(time=request.form['time'], side=request.form['side'], fast_break=request.form['fast break'])
    db.session.add(track1)
    db.session.commit()

    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)