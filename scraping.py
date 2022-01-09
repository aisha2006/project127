from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import requests
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(START_URL)
print(page)

soup = BeautifulSoup(page.text, "html.parser")
star_table = soup.find("table")
temp_list = []
table_rows = star_table.find_all("tr")
for i in table_rows:
    td = i.find_all("td")
    row = [j.text.rstrip() for j in td]
    temp_list.append(row)

star_names = []
mass = []
distance = []
radius = []
lum = []

for i in range(1,len(temp_list)):
    star_names.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    lum.append(temp_list[i][7])
    radius.append(temp_list[i][6])

df = pd.DataFrame(list(zip(star_names, distance, mass, radius, lum)), columns = ["star_name", "distance", "mass", "radius", "luminosity"])
df.to_csv("Brightstars.csv")