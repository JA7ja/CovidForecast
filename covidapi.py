import requests
class Covid():
    def __init__(self, type, name):
        self.type = type
        if self.type == "country":
            self.state = "countries/"
        elif self.type == "state":
            self.state = "states/"
        elif self.type == "county":
            self.state = "jhucsse/counties/"
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
        if self.type == "county":
            self.confirmed_cases = self.response[0]["stats"]["confirmed"]
            self.deaths = self.response[0]["stats"]["deaths"]
            self.recovered = self.response[0]["stats"]["recovered"]
        elif self.type == "state" or "country":
            self.confirmed_cases = self.response["cases"]
            self.today_cases = self.response["todayCases"]
            self.today_deaths = self.response["todayDeaths"]
            self.recovered = self.response["recovered"]
            self.active_cases = self.response["active"]
            self.deaths = self.response["deaths"]
            self.deaths_per_million = self.response["deathsPerOneMillion"]
    def __str__(self):
        if self.type == "county":
            confirm_cases = "Confirm cases : " + str(self.confirmed_cases)
            recovered = " Number of recovered: " + str(self.recovered)
            deaths = " Number Of deaths: " + str(self.deaths)
            string = confirm_cases + deaths + recovered
        elif self.type == "country" or state:
            confirm_cases = "Confirm cases : " + str(self.confirmed_cases)
            today_cases = " Today's cases : " + str(self.today_cases)
            today_death = " Today's Deaths : " + str(self.today_deaths)
            recovered = " Number of recovered: " + str(self.recovered)
            active_cases =  " Active cases : " + str(self.active_cases)
            deaths = " Number Of deaths: " + str(self.deaths)
            deaths_per_million = " Deaths Per Million : " + str(self.deaths_per_million)
            string = confirm_cases + today_cases + today_death + recovered + active_cases + death + death_per_million
        return string

covid = Covid("county", "Jackson")
print(covid)
