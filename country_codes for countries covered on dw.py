# use this function to create a csv of the country codes for the countries covered on dw
import requests
from bs4 import BeautifulSoup
import pandas as pd
r = requests.get("https://www.dw.com/sitemap.xml")
soap = BeautifulSoup(r.content, "lxml")
countries = soap.find_all("loc")
country_codes = []
for country in countries:
    code = country.text.split("com/")[1].split("/")[0]
    if code not in country_codes:
        country_codes.append(code)
df = pd.DataFrame(country_codes)
df.to_csv("country_codes", index=False)
