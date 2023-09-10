import requests
import time
import os
from dotenv import load_dotenv
import array as ar
import pandas as pd

load_dotenv()
#-------------Functions-------------
#EXAMPLE ON HOW TO CALL ->      os.getenv('client_id')

os.getenv('')

def divide_area(southwest_lat, southwest_lon, northeast_lat, northeast_lon, n):
    # Calculate latitude and longitude step sizes
    lat_step = (northeast_lat - southwest_lat) / n
    lon_step = (northeast_lon - southwest_lon) / n
    
    # Initialize a list to store the divided areas
    divided_areas = []

    for i in range(n):
        # Calculate the coordinates for each box
        box_southwest_lat = southwest_lat + i * lat_step
        box_southwest_lon = southwest_lon
        box_northeast_lat = box_southwest_lat + lat_step
        box_northeast_lon = northeast_lon
        
        # Create a formatted string for the box's coordinates
        box_coordinates = f"{box_southwest_lat}, {box_southwest_lon}, {box_northeast_lat}, {box_northeast_lon}"
        
        # Append the box coordinates to the list
        divided_areas.append(box_coordinates)

    return divided_areas

#-------------Main-------------
#Df creation, changed from txt file     8/24

#DF Creation, create temp and hold data in df_segments
columns =['SegName','SegNum']
df=pd.DataFrame(columns=columns)
df_Segments=df.astype({"SegNum":'int64'},copy=False)

#bounds =  # array[Float] | [southwest corner latitutde, southwest corner longitude, northeast corner latitude, northeast corner longitude]
tempListLocations="40.60034008410533, -73.9948294872619,40.65157646433741, -73.92683111672085"
#tempListLocations='40.5411, -74.04795, 40.5437511, -74.0450481'
# ne=(40.80621,-73.75776)
# sw=(40.54110,-74.04795)



#Timer vars to work under API limits
maxRequests=100
timerInterval=15*60
requestCount=0
startTime=time.time()


# Set the API endpoint
api_url = 'https://www.strava.com/api/v3/segments/explore'

#n= number of split areas created in larger map
n=5
coordList=divide_area(40.54110,-74.04795,40.80621,-73.75776, n)
# coordList=divide_area(40.70419691822427, -73.81544109047971,40.73312306812104, -73.78282145859072,n)

# for i in range(5):
#     print(cordListFinal[i])
# Set other parameters for the explore request (optional)
radius = 1000  # in meters
min_cat = 0   # minimum climb category (0-5)
max_cat = 56   # maximum climb category (0-5)
  
for coord in coordList:
    currentTime=time.time()
    if currentTime - startTime >= timerInterval:
        startTime=currentTime
        requestCount=0

    if requestCount>= maxRequests:
        print("***15 Minute max Reached... Waiting ***")
        time.sleep(timerInterval - (currentTime-startTime))
        startTime=time.time()
        request_count=0

    headers = {'Authorization': f'Bearer {os.getenv("access_token")}'}
    params = {
        #'bounds':tempListLocations,    SMALL TEST LOCATION (Brooklyn)
        'bounds':coordList,
        'activity_type': 'riding',
        }

    response = requests.get(api_url, headers=headers, params=params)

    # Process the response
    if response.status_code == 200:
        data = response.json()
        for segment in data['segments']:
            segment_name = segment['name']
            segment_id = segment['id']
            df_Temp=pd.DataFrame({'SegName': [segment_name],'SegNum':[segment_id]})
            df_Segments=pd.concat([df_Segments,df_Temp],ignore_index=True,axis=0)
            print(f'Segment Name: {segment_name}')
            print(f'Segment ID: {segment_id}')
    else:
        print(f'Error: {response.status_code} - {response.text}')

    requestCount+=1
    time.sleep(1)

df_Segments.to_csv('saved_seg_data2.csv.csv', index=False)
