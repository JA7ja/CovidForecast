import requests
# class Covid():
#     def __init__(self, country, status):
#         self.base_url = "https://covid-api.mmediagroup.fr/v1"
#         self.country = "?country="+ str(country)
#         self.status = "&status=" + str(status)
#     def get(self):
#         self.requesturl = self.base_url + self.country + self.status
#         self.request = requests.get(self.requesturl)
#         self.response = self.request.json
#     def response(self):
#         print(self.response)
#     def __str__(self):
#         return null
#
# covid = Covid("France", "cases")
def covid(country, status):
    base_url = "https://covid-api.mmediagroup.fr/v1"
    select_country = "?country="+ str(country)
    status = "&status=" + str(status)
    url = base_url + select_country + status
    request = requests.get(url)
    response = request.json
covid("France", "cases")
