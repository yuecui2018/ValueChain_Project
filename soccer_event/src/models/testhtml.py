from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)

@app.route('/', methods = ['GET'])
def parser():
 return render_template('index.html')
@app.route('/', methods = ['POST'])
def model():
  #test = request.form['side']
  test = request.form['body part']
  if (test == 'left foot'):
    return '<h3> test succeed</h3>'
  else:
    return '<h3> invalid </h3>'


if __name__ == '__main__':
	app.run()
