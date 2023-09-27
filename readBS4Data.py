from bs4 import BeautifulSoup
import json



#HTML held in txt for production and testing
with open('myOutFile.txt', 'r',encoding="utf-8") as f:
    html_data = f.read()

#create soup obj
soup = BeautifulSoup(html_data, 'html.parser')

rows = soup.select('tbody tr')

#go throguh rows
#TODO: save vars into DF with segment location(segment Number)
for row in rows:
    
    data_properties = row.find('td', {'class': 'athlete track-click'})['data-tracking-properties']
    athlete_id = int(data_properties.split('"athlete_id":')[1].split(',')[0])
    rank = int(data_properties.split('"rank":')[1].split('}')[0])

    # athlete name, date, speed, and time
    athlete_name = row.find('td', {'class': 'athlete track-click'}).a.text
    date = row.find_all('td', {'class': 'track-click'})[1].a.text
    speed = float(row.find_all('td')[3].text.split()[0])
    time = row.find('td', {'class': 'last-child'}).text
    
    print(f"Athlete ID: {athlete_id}, Rank: {rank}")
    print(f"Name: {athlete_name}, Date: {date}, Speed: {speed}, Time: {time}\n")

