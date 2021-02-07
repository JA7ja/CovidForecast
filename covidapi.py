import requests
class Covid():
    def __init__(self, type, name):
        self.type = type
        if self.type == "country":
            self.state = "countries/"
        if self.type == "state":
            self.state = "states/"
        self.base_url = "https://corona.lmao.ninja/v2/"
        self.name_of_place = str(name)
        self.confirmed_cases = 0
        self.today_cases = 0
        self.today_deaths = 0
        self.recovered = 0
        self.active_cases = 0
        self.deaths = 0
        self.life_expectancy = 0
        self.get()
    def get(self):
        self.requesturl = self.base_url + self.state + self.name_of_place
        self.request = requests.get(self.requesturl)
        self.response = self.request.json()
        self.confirmed_cases = self.response["cases"]
        self.today_cases = self.response["todayCases"]
        self.today_deaths = self.response["todayDeaths"]
        self.recovered = self.response["recovered"]
        self.active_cases = self.response["active"]
        self.deaths = self.response["deaths"]
        self.deaths_per_million = self.response["deathsPerOneMillion"]
    def __str__(self):
        string = "Confirm cases : " + str(self.confirmed_cases) + " Today's cases : " + str(self.today_cases) + " Today's Deaths : " + str(self.today_deaths) + " Number of recovered: " + str(self.recovered) + " Active cases : " + str(self.active_cases) + " Number Of deaths: " + str(self.deaths) + " Deaths Per Million : " + str(self.deaths_per_million)
        return string

covid = Covid("state", "New York")
print(covid)
