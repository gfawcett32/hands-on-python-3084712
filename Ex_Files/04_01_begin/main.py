import requests # a third-party library used for making HTTP requests to interact with web resources i.e. web APIs, websites. and web services.

response = requests.get(
    "http://api.worldbank.org/v2/countries/USA/indicators/SP.POP.TOTL?per_page=5000&format=json")

last_twenty_years = response.json()[1][:20]
