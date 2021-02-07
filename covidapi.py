import requests
class Covid():
    def __init__(self, country):
        self.base_url = "https://covid-api.mmediagroup.fr/v1/cases"
        self.country = "?country="+ str(country)
        self.confirmed_cases = 0
        self.recovered = 0
        self.deaths = 0
        self.life_expectancy = 0
        self.get()
    def get(self):
        self.requesturl = self.base_url + self.country
        self.request = requests.get(self.requesturl)
        self.response = self.request.json()
        self.confirmed_cases = self.response["All"]["confirmed"]
        self.recovered = self.response["All"]["recovered"]
        self.deaths = self.response["All"]["deaths"]
        self.life_expectancy = self.response["All"]["life_expectancy"]
    def __str__(self):
        string = "Confirm cases : " + str(self.confirmed_cases) + " Number of recovered: " + str(self.recovered) + " Number Of deaths: " + str(self.deaths) + " Life expectancy: " + str(self.life_expectancy)
        return string



covid = Covid("Germany")
print(covid)
