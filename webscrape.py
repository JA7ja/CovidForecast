from bs4 import BeautifulSoup
import requests

def get_cdc_guidelines():
    cdc_text = requests.get('https://cdc.gov/coronavirus/2019-ncov/prevent-getting-sick/prevention.html').text
    parser = BeautifulSoup(cdc_text, "html.parser")

    rec2 = parser.find_all("h2", {"class": "card-title h3 mb-2 text-left"})
    rec3 = parser.find_all("h3")

    cdc_recs_raw = rec2 + rec3
    cdc_recs = []

    for i in range(0, len(cdc_recs_raw)-2):
        cdc_recs.append(cdc_recs_raw[i].text)

    return cdc_recs


def get_who_guidelines():

    who_text = requests.get('https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public').text
    parser = BeautifulSoup(who_text, "html.parser")

    who_recs_raw = parser.find_all("strong")
    who_recs = []

    for i in range(6, len(who_recs_raw)):
        
        if(who_recs_raw[i].text != "" and who_recs_raw[i].text != " " and who_recs_raw[i].text != "."):
            who_recs.append(who_recs_raw[i].text)

    return who_recs
