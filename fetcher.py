# use this function to fetch the recent news of a certain country from the database and save it to a csv file
import sqlite3
import pandas as pd


def fetcher(country_code):
    conn = sqlite3.connect("world news.db")
    df = pd.read_sql_query(f"SELECT * FROM {country_code}", conn)
    df.to_csv(f"{country_code} sites")

# using Deutschland code as an example


fetcher("de")
