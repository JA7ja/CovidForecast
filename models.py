from os import path
import covidapi
import historicalapi
ROOT = path.dirname(path.relpath((__file__)))

def confirmCases(type, name):
    detect_case = Covid(type, name)
    return detect_case.confirmed_cases
def deaths(type, name):
    detect_case = Covid(type, name)
    return detect_case.deaths
def recovered(type, name):
    detect_case = Covid(type, name)
    return detect_case.recovered
def todayCases(type, name):
    detect_case = Covid(type, name)
    return detect_case.today_cases
def todayDeaths(type, name):
    detect_case = Covid(type, name)
    return detect_case.today_deaths
def deaths_per_million(type, name):
    detect_case = Covid(type, name)
    return detect_case.deaths_per_million
def historicalapi(type, name, days):
    detect_case = Historical(type, name, days)
    return detect_case
