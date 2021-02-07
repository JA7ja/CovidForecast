from bs4 import BeautifulSoup
import requests

cdc_text = requests.get('https://cdc.gov/coronavirus/2019-ncov/prevent-getting-sick/prevention.html').text
who_text = requests.get('https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public').text

parser = BeautifulSoup(cdc_text, "html.parser")

rec2 = parser.find_all("h2", {"class": "card-title h3 mb-2 text-left"})
rec3 = parser.find_all("h3")

cdc_recs = rec2 + rec3

parser = BeautifulSoup(who_text, "html.parser")

who_recs = parser.find_all("strong")

print("CDC Guidelines:")
for i in range(0, len(cdc_recs)-2):
    print(cdc_recs[i].text)

print("")
print("WHO Guidelines:")
for i in range(6, len(who_recs)):
    if(who_recs[i].text != "" and who_recs[i].text != " " and who_recs[i].text != "."):
        print(who_recs[i].text)