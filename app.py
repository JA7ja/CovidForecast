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

    error = None

    #GET just displays the page
    if request.method == 'GET':
        pass

    #POST gives us the country, state, and county
    if request.method == 'POST':
        country = request.form.get('country')
        state = request.form.get('state')
        county = request.form.get('county')
        session['country'] = country
        session['state'] = state
        session['county'] = county

        if country != "":
            if country != "United States" or state == "":
                session['type'] = 'country'
            elif county == "":
                session['type'] = 'state'
            else:
                session['type'] = 'county'

            return redirect('/cases.html')
        else:
            error = "Please enter a country."

    #Displays the HTML
    return render_template('home.html', error=error)

#Cases page
@app.route('/cases.html', methods=['GET'])
def cases():

    #GET just displays the page
    if request.method == 'GET':
        #If the user has not defined a zip, they will be redirected to the home page
        if 'country' not in session:
            return redirect('/home.html')

    #int
    total_cases = confirmCases(session['type'], session[session['type']])
    #int
    today_cases = todayCases(session['type'], session[session['type']])
    #int
    deaths_p_million = deaths_per_million(session['type'], session[session['type']])
    #list of ints (14)
    historical_data = historicalapi(session['type'], session[session['type']], 14)

    #Displays the HTML
    return render_template('cases.html', total_case=total_cases, today_case=today_cases, deaths_per_million=deaths_p_million, historical_data_cases=historical_data)

#Info page
@app.route('/info.html', methods=['GET'])
def info():

    #GET just displays the page
    if request.method == 'GET':
        pass

    #list of strings
    who_guidelines = get_who_recs()
    #list of strings
    cdc_guidelines = get_cdc_recs()

    #Displays the HTML
    return render_template('info.html', who=who_guidelines, cdc=cdc_guidelines)

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
