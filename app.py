from flask import Flask, render_template, request
from flask_cors import CORS
from models import *

app = Flask(__name__)
CORS(app)

#Home page
@app.route('/home', methods=['GET', 'POST'])
def home():
    
    #GET just displays the page
    if request.method == 'GET':
        pass

    #POST gives us the zip code of the user
    if request.method == 'POST':
        zip = request.form.get('zipcode')

        #needs implementing in models
        #get_covid_data(zip)

    #Displays the HTML
    return render_template('home.html')

#Cases page
@app.route('/cases', methods=['GET'])
def cases():

    #GET just displays the page
    if request.method == 'GET':
        pass

    #Displays the HTML
    return render_template('cases.html')

#Info page
@app.route('/info', methods=['GET'])
def info():

    #GET just displays the page
    if request.method == 'GET':
        pass

    #Displays the HTML
    return render_template('info.html')

#Vaccine page
@app.route('/vaccine', methods=['GET'])
def vaccine():

    #GET just displays the page
    if request.method == 'GET':
        pass

    #Displays the HTML
    return render_template('vaccine.html')


#To run the website, enter: 'FLASK_APP=app.py flask run' into the console in the repository