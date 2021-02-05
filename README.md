# Covid 19 Xray image classifier

This is a web app that helps us to classify images of chest Xrays as covid positive or negative and also tells us the existence of Pneumonia in lungs.

## Built With 
- Python
- DropzoneJS
- Flask
- Flask-SQLAlchemy
- CSS
- HTML 

## To run the app

First get the project
`git clone https://github.com/jod35/covid-19-xray-image-classifier.git`

Then 
`cd covid-x-ray-image-classifier`

Then create a Python Virtual Environment using your preferred way for example,
`python -m venv env ` 

Activate the virtual environment with 
`source /env/bin/activate`

Within your virual environment, install all the requirements with 
`pip install -r requirements.txt`

Finally run with

`export FLASK_APP=wsgi.py` then `flask run `

If you need to view debug messages, `export FLASK_DEBUG =1` to set the Flask debug mode on

## How it works
Given an image which is of a chest Xray, we can predict Covid-19 severity as well as severity of other diseases like Pneumonia.

## Contribution

I need your help guys please help.
