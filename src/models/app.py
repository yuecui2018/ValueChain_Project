from flask import Flask
from flask import request
from flask import render_template
import pickle
import os
import pandas as pd
import statsmodels.api as sm
import logging

logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('soccer_event.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)


app = Flask(__name__)

@app.route('/', methods = ['GET'])
def parser():
  """
  Initialize the webpage
  """
  return render_template('index.html')
@app.route('/', methods = ['POST'])

def model():
  """
  Render the webpage and fead values from inputs on the website and return the predicted result, which will be showned on the web page.
  """
  time = int(request.form['time'])
  side_val = request.form['side']
  event_val = request.form['event_type']
  assist_val = request.form['assist_method']
  fastbreak_val = request.form['fastbreak']

  if (side_val == 'home'):
    side_2 = 1
  else:
    side_2 = 0
  
  if (event_val == "event_type_Corner"):
    event_type_Corner = 1
    event_type_FreeKick = event_type_Attempt = event_type_Card = event_type_other = event_type_Foul = 0
  elif (event_val == "event_type_FreeKick"):
    event_type_FreeKick = 1
    event_type_Corner = event_type_Attempt = event_type_Card = event_type_other = event_type_Foul = 0
  elif (event_val == "event_type_Attempt"):
    event_type_Attempt = 1
    event_type_Corner = event_type_FreeKick = event_type_Card = event_type_other = event_type_Foul = 0
  elif (event_val == "event_type_Card"):
    event_type_Card = 1
    event_type_Corner = event_type_FreeKick = event_type_Attempt = event_type_other = event_type_Foul = 0
  elif (event_val == "event_type_other"):
    event_type_other = 1
    event_type_Corner = event_type_FreeKick = event_type_Attempt = event_type_Card = event_type_Foul = 0
  else:
    event_type_Foul = 1
    event_type_Corner = event_type_FreeKick = event_type_Attempt = event_type_Card = event_type_other = 0	

  if (assist_val == 'yes'):
    assist_method_Pass = 1
  else:
    assist_method_Pass = 0   

  if (fastbreak_val == 'yes'):
    fast_break_1 = 1
  else:
    fast_break_1 = 0   

  pred_list = [event_type_FreeKick,event_type_Corner,event_type_Attempt,time,assist_method_Pass,
  event_type_Foul,event_type_Card,side_2,event_type_other,fast_break_1]
  
  logger.info("Users' input are successfully captured. Inputs are: %s" % str(pred_list))
  ###Predict result using the pickle file
  mymodel=pickle.load(open('result.p',"rb"))
  pred_prob= round(float(mymodel.predict(pred_list)),2)

  logger.info("The probability is successfully predicted, which is: %s" % str(pred_prob))
  return render_template("index.html", prob = pred_prob)

if __name__ == '__main__':
    app.run()
