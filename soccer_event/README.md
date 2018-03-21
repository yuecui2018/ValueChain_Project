soccer_event
==============================


**Vision**: The objective of this project is to help players understand what is the probability of a shot being a goal. Many specific attributes regarding the shots, such as team, assist method,  shot location, number of players on the pitch…etc., will be taken into account.

**Mission**: Help players to better forecast if a shot will be on target using the dataset that includes totaling 941,009 events from the biggest 5 European football (soccer) leagues from 2011/2012 season to 2016/2017 season.

**Success criteria**: A web app that will show the predicted probability of a shot being a goal after user inputs values for a set of attributes.


Steps
--------------

### Set up Environment
### Go to `soccer_event/` folder, run
> source ./py/bin/activate
> pip install -r requirement.txt

### Run App
> cd ../src/models/
> python app.py

Project Organization
--------------

├── LICENSE
│
├── README.md          <- The top-level README for developers using this project.
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g. generated with `pip freeze > requirements.txt`
│
├── py                 <- virtualenv files
│
├── result.p           <- pickles file to store the model
│
├── models             <- script to train model
│
├── database           <- Files used to create database and store data
│
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── templates      <- HTML file.
│   │   │
│   │   ├── basic.css
│   │
│   ├── static         <- Scripts to train models and then use trained models to make predictions
│   │   │
│   │   ├── basic.css
│   │   └── index.js
│   │
│   │
│   ├── database       <- Scripts to download and generate data
│   │
│   └──  models
│       │
│       ├── app.py         <- File required to run the app.
│       └── __init__.py    <- Makes src a Python module
│
│
├── docs               <- A default Sphinx project; see sphinx-doc.org for details

Link to download the data
--------------
https://www.kaggle.com/secareanualin/football-events/data

Link to pivotal tracker
--------------
https://www.pivotaltracker.com/n/projects/2144262




