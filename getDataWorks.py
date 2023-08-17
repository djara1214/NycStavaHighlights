import requests
import os
from dotenv import load_dotenv
import array as ar
load_dotenv()
#-------------Functions-------------
#EXAMPLE ON HOW TO CALL ->      os.getenv('client_id')

os.getenv('')

def divide_area(sw_lat, sw_lon, ne_lat, ne_lon, n):
    coordinates = []
    
    lat_range = ne_lat - sw_lat
    lon_range = ne_lon - sw_lon
    
    lat_step = lat_range / n
    lon_step = lon_range / n
    
    for i in range(n):
        for j in range(n):
            new_sw_lat = sw_lat + i * lat_step
            new_sw_lon = sw_lon + j * lon_step
            new_ne_lat = new_sw_lat + lat_step
            new_ne_lon = new_sw_lon + lon_step
            coordinates.append(f'"{new_sw_lat},{new_sw_lon},{new_ne_lat},{new_ne_lon}"')
    
    return coordinates



#-------------Main-------------
# tempListLocations="40.60034008410533, -73.9948294872619,40.65157646433741, -73.92683111672085"
#tempListLocations='40.5411, -74.04795, 40.5437511, -74.0450481'
# ne=(40.80621,-73.75776)
# sw=(40.54110,-74.04795)
n=10

# Set the API endpoint
api_url = 'https://www.strava.com/api/v3/segments/explore'

coordList=divide_area(40.54110,-74.04795,40.80621,-73.75776, n)


# for i in range(5):
#     print(cordListFinal[i])
# Set other parameters for the explore request (optional)
radius = 1000  # in meters
min_cat = 0   # minimum climb category (0-5)
max_cat = 56   # maximum climb category (0-5)


with open("segmentList.txt",'a') as file:

    for location in coordList:
        headers = {'Authorization': f'Bearer {os.getenv("access_token")}'}
        params = {
            'bounds':location,
            'activity_type': 'riding',
            }

        response = requests.get(api_url, headers=headers, params=params)

        # Process the response
        if response.status_code == 200:
            data = response.json()
            for segment in data['segments']:
                segment_name = segment['name']
                segment_id = segment['id']
                # print(f'Segment Name: {segment_name}')
                # print(f'Segment ID: {segment_id}')
                file.write(str(segment_id)+ '\n')
        else:
            print(f'Error: {response.status_code} - {response.text}')