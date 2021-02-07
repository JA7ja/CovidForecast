import requests
class Covid():
    def __init__(self, type, name):
        try:
            self.type = type.lower()
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
            self.deaths_per_million = 0
            self.get()
        except AttributeError:
            print("Your Country, County, or State does not exist!")
    def get(self):
        try:
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
        except KeyError:
            print("Your Country, County, or State does not exist!")
    def __str__(self):
            try:
                if self.type == "county":
                    confirm_cases = "Confirm cases : " + str(self.confirmed_cases)
                    recovered = " Number of recovered: " + str(self.recovered)
                    deaths = " Number Of deaths: " + str(self.deaths)
                    string = confirm_cases + deaths + recovered
                elif self.type == "country" or "state":
                    confirm_cases = "Confirm cases : " + str(self.confirmed_cases)
                    today_cases = " Today's cases : " + str(self.today_cases)
                    today_death = " Today's Deaths : " + str(self.today_deaths)
                    recovered = " Number of recovered: " + str(self.recovered)
                    active_cases =  " Active cases : " + str(self.active_cases)
                    deaths = " Number Of deaths: " + str(self.deaths)
                    deaths_per_million = " Deaths Per Million : " + str(self.deaths_per_million)
                    string = confirm_cases + today_cases + today_death + recovered + active_cases + deaths + deaths_per_million
                return string
            except:
                string = "Your Country, County, or State does not exist!"
                return string

class Historical():
    def __init__(self, type, name, days):
        try:
            self.type = type.lower()
            self.days = str(days)
            self.base_url = "https://corona.lmao.ninja/v2/historical/"
            self.name_of_place = str(name)
            self.get()
        except AttributeError:
            print("Your Country, County, or State does not exist!")
    def get(self):
        try:
            if self.type == "country":
                self.requesturl = self.base_url + self.name_of_place + "?lastdays=" + self.days
            elif self.type == "state":
                self.requesturl = self.base_url + "usacounties/" + self.name_of_place + "?lastdays=" + self.days
            self.request = requests.get(self.requesturl)
            self.response = self.request.json()
        except KeyError:
            print("Your Country, County, or State does not exist!")
    def __str__(self):
        list_of_dates_and_cases = []
        dates_and_cases = self.response["timeline"]["cases"].copy()
        list_of_dates_and_cases.append(dates_and_cases)
        for date in list_of_dates_and_cases:
            return str(date)
test = Historical("country", "United States", 14)
print(test)
