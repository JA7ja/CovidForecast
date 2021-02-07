import requests
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
            print(self.response)
        except KeyError:
            print("Your Country, County, or State does not exist!")

covid = Covid("state", "new york", 14)
