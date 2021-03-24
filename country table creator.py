import requests
from bs4 import BeautifulSoup
import sqlite3
# use this function to create or update a table of a certain country's recent news in an sql database


def country_table_maker(country_code):
    url = f"https://www.dw.com/{country_code}/sitemap-news.xml"
    r = requests.get(url)
    soap = BeautifulSoup(r.content, "lxml")
    data = soap.find_all("url")
    sites_parsed = []
    for item in data:
        site = {
            "title": item.find("news:title").text,
            "publication_date": item.find("news:publication_date").text,
            "url": item.find("loc").text
        }
        sites_parsed.append(site)
    conn = sqlite3.connect("world news.db")
    c = conn.cursor()
    try:
        c.execute(f'''DROP TABLE {country_code}''')
    except:
        c.execute(f'''CREATE TABLE {country_code}(title TEXT, publication date TEXT, url TEXT)''')
    else:
        c.execute(f'''CREATE TABLE {country_code}(title TEXT, publication date TEXT, url TEXT)''')
    for site in sites_parsed:
        title = site["title"]
        publication_date = site["publication_date"]
        url = site["url"]
        c.execute(f'''INSERT INTO {country_code} VALUES(?,?,?)''', (title, publication_date, url))
    conn.commit()
    conn.close()

# using Deutschland code as an example


country_table_maker("de")
