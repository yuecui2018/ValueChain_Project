# Soccer Goal Predicting App
==============================

```
**Vision**: The objective of this project is to help players understand what is the probability of a shot being a goal. Many specific attributes regarding the shots, such as team, assist method,  shot location, number of players on the pitch…etc., will be taken into account.

**Mission**: Help players to better forecast if a shot will be on target using the dataset that includes totaling 941,009 events from the biggest 5 European football (soccer) leagues from 2011/2012 season to 2016/2017 season.

**Success criteria**: A web app that will show the predicted probability of a shot being a goal after user inputs values for a set of attributes.
```


Steps to deploy the app
------------
```
### Set up Environment
### Go to `soccer_event/` folder, run
> source ./py/bin/activate
> pip install -r requirement.txt

### Run App
> cd ../src/models/
> python app.py
```


Project Organization
------------

    ├── LICENSE
    │
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    │
    ├── README.md          <- The top-level README for developers using this project.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │   │
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   │     
    │   ├── static         <- CSS and JavaScript files
    │   │ 
    │   ├── templates      <- HTML file
    │   │   
    │   ├── models         
    │       ├── app.py     <- File required to run the app.
    │       └── __init__.py <- Makes src a Python module
    │   
    │
    ├── database           <- Files used to create database and store data
    │
    ├── models             <- script to train model
    │


Link to download the data
------------
https://www.kaggle.com/mirosval/personal-cars-classifieds/data


Link to Pivotal Tracker
------------
https://www.pivotaltracker.com/n/projects/2143346

