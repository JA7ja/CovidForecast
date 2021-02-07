from flask import Flask, render_template, request, redirect, session
from flask_cors import CORS
from models import *

app = Flask(__name__)
app.secret_key = "HACKBU 2021"
CORS(app)

#Landing page (reroutes to Home automatically)
@app.route('/', methods=['GET'])
def landing():

    if request.method == 'GET':
        return redirect('/home.html')

#Home page
@app.route('/home.html', methods=['GET', 'POST'])
def home():
    
    #GET just displays the page
    if request.method == 'GET':
        pass

    #POST gives us the country, state, and county
    if request.method == 'POST':
        country = request.form.get('country')
        print(country)
        state = request.form.get('state')
        print(state)
        county = request.form.get('county')
        print(county)
        session['country'] = country
        session['state'] = state
        session['county'] = county
        return redirect('/cases.html')
        #needs implementing in models
        #get_covid_data(zip)

    #Displays the HTML
    return render_template('home.html')

#Cases page
@app.route('/cases.html', methods=['GET'])
def cases():

    #GET just displays the page
    if request.method == 'GET':
        #If the user has not defined a zip, they will be redirected to the home page
        if 'country' not in session:
            return redirect('/home.html')

    #Displays the HTML
    return render_template('cases.html')

#Info page
@app.route('/info.html', methods=['GET'])
def info():

    #GET just displays the page
    if request.method == 'GET':
        pass

    #Displays the HTML
    return render_template('info.html')

#Vaccine page
@app.route('/vaccine.html', methods=['GET'])
def vaccine():

    #GET just displays the page
    if request.method == 'GET':
        #If the user has not defined a zip, they will be redirected to the home page
        if 'country' not in session:
            return redirect('/home.html')

    #Displays the HTML
    return render_template('vaccine.html')


#To run the website, enter: 'FLASK_APP=app.py flask run' into the console in the repository