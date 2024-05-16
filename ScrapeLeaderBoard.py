#Code for stava cookies found on 9/27/23 @ https://github.com/dalacost/strava_hack_tools/blob/44300403012b53ee17e397f4fe2023846dea7f82/strava_hack_tools_common/login.py
#Thankyou to Dalacost for helping my code stay loggedin to Stava.com
import requests
from http.cookiejar import LWPCookieJar
import os
from bs4 import BeautifulSoup
import pandas as pd
from dotenv import load_dotenv
from random import randint
from time import sleep


STRAVA_URL_LOGIN                = 'https://www.strava.com/login'
STRAVA_URL_SESSION              = 'https://www.strava.com/session'
STRAVA_ACTIVITIES_SESSION       = 'https://www.strava.com/activities/'
STRAVA_LOGGED_OUT_FINGERPRINT   = 'logged-out'
COOKIE_FILE_DIR                 = '.authdata'
load_dotenv()

class Login:

    VERBOSE = False
    LOGIN_SESSION = ''
    AUTHENTICITY_TOKEN = ''

    def __init__(self, verbose=False):
        self.VERBOSE = verbose

    def cookies_save_to_disk(self, login_username,session,authenticity_token):
        session.cookies.save(ignore_discard=True)
        file = open(COOKIE_FILE_DIR+'_'+str(login_username)+'_authenticity_token', 'w')
        file.write(authenticity_token)
        file.close()


    def cookies_remove_from_disk(self, login_username):
        if os.path.exists(COOKIE_FILE_DIR+'_'+str(login_username)):
            os.remove(COOKIE_FILE_DIR+'_'+str(login_username))

        if os.path.exists(COOKIE_FILE_DIR+'_'+str(login_username)+'_authenticity_token'):
            os.remove(COOKIE_FILE_DIR+'_'+str(login_username)+'_authenticity_token')

    def cookies_get_from_disk(self, login_username, session):
        if self.VERBOSE:
                print('loading saved cookies')
        session.cookies.load(ignore_discard=True)
        file = open(COOKIE_FILE_DIR+'_'+str(login_username)+'_authenticity_token', 'r')
        authenticity_token = file.read()
        file.close()
        return authenticity_token

    def forcelogin(self, login_username):
        if self.VERBOSE:
            print('Force a new login...')
        self.cookies_remove_from_disk(login_username)


    def login(self, login_username, login_password):

        columns =["seg_num",'athlete_id','athlete_name','rank','speed','time','date']
        df_scrape=pd.DataFrame(columns=columns)
        all_segments_logged_in = True

       
        # Read in Segment List and leaderBoard data Scrapped so far
        df_api=pd.read_csv("Seg_with_poly.csv")
        df_scrape=pd.read_csv('scrapeTest_STRAVA_withDf_1.csv')

        session = requests.session()
        session_from_disk = False

        session.cookies = LWPCookieJar(COOKIE_FILE_DIR+'_'+str(login_username))
        if os.path.exists(COOKIE_FILE_DIR+'_'+str(login_username)):
            # Load saved cookies from the file and use them in a request
            authenticity_token= self.cookies_get_from_disk(login_username, session)		
            session_from_disk = True
        else:
            r = session.get(STRAVA_URL_LOGIN)
            soup = BeautifulSoup(r.content, 'html.parser')

            get_details = soup.find('input', attrs={'name':'authenticity_token'})
            authenticity_token = get_details.attrs.get('value')

            if self.VERBOSE:
                print('LOGIN TOKEN:'+authenticity_token)
            
            # This is the form data that the page sends when logging in
            login_data = {
                'email': os.getenv('my_email'),
                'password': os.getenv('my_password'),
                'utf8': '%E2%9C%93',
                'authenticity_token':authenticity_token
            }

            # Authenticate
            r = session.post(STRAVA_URL_SESSION, data=login_data)
            self.cookies_save_to_disk(login_username, session, authenticity_token)

        #Go through user defined rows in the Segment Df
        #Only did about 100-150 at a time to avoid detection 
        for counter, APIrow in df_api.iloc[1249:1353].iterrows():
            try:
                segmentNumber=APIrow['SegNum']
                addr='https://www.strava.com/segments/'
                addr_full=addr+str(segmentNumber)
                print("addr being contacted: "+ str(addr_full))
                timeToSleep=randint(32,65)
                sleep(timeToSleep)
                #accessing a page that requires you to be logged in
                r = session.get(addr_full)

                self.LOGIN_SESSION = session
                self.AUTHENTICITY_TOKEN = authenticity_token
                #Grab HTML data from visted webpage 
                soup = BeautifulSoup(r.content, 'html.parser')
                rows = soup.select('tbody tr')

                #go through html and grab all relevant leaderboard data
                for row in rows:
                    data_properties = row.find('td', {'class': 'athlete track-click'})['data-tracking-properties']
                    athlete_id = int(data_properties.split('"athlete_id":')[1].split(',')[0])
                    rank = int(data_properties.split('"rank":')[1].split('}')[0])

                    # athlete name, date, speed, and time
                    athlete_name = row.find('td', {'class': 'athlete track-click'}).a.text
                    date = row.find_all('td', {'class': 'track-click'})[1].a.text
                    speed = float(row.find_all('td')[3].text.split()[0])
                    time = row.find('td', {'class': 'last-child'}).text

                            #Testing - display data for current page 
                    # print("current Segment is ",str(segmentNumber) )
                    # print("Counter: ",str(counter))
                    #print(f"Athlete ID: {athlete_id}, Rank: {rank}")
                    #print(f"Name: {athlete_name}, Date: {date}, Speed: {speed}, Time: {time}\n")
                    #['athlete_id','athlete_name','rank','speed','time','date',"seg_num"]

                    df_Temp_scrape=pd.DataFrame({'SegNum':[segmentNumber],'athlete_id': [athlete_id],'athlete_name':[athlete_name],'rank':[rank],'speed':[speed],'time':[time],'date':[date]})
                    df_scrape=pd.concat([df_scrape,df_Temp_scrape],ignore_index=True,axis=0)
                
                print("current Segment is ",str(segmentNumber) )
                print("Counter: ",str(counter))
                print("Sleeping: ",str(timeToSleep))
                #if error occurs, the error itself, segment number, and current iteration that gave error is appended to log file
            except Exception as e:
                with open("LOG_FILE.text",'a') as file:
                    file.write(f"Segment Number: {segmentNumber} \nCounter Iteration: {counter}\nError is:  {e}")
                    continue
           

            if int(r.text.find(STRAVA_LOGGED_OUT_FINGERPRINT)) >= 0:
                if session_from_disk:
                    if self.VERBOSE:
                        print('Saved cookies Failed, getting new session data...')
                    self.cookies_remove_from_disk(login_username)
                    all_segments_logged_in = False  # Set the flag to False
                else:
                    all_segments_logged_in = False  # Set the flag to False

        #Append new data to end of old data
        df_scrape.to_csv("scrapeTest_STRAVA_withDf_1.csv", sep=',', index=False, encoding='utf-8')
        return all_segments_logged_in

# Create an instance of the Login class
strava_login = Login(verbose=True)

#Strava login credentials
login_username = os.getenv('my_email')
login_password = os.getenv('my_password')

# call login method
logged_in = strava_login.login(login_username, login_password)

if logged_in:
    print("Successfully scraped data, current loop has terminated!")
else:
    print("Login failed. Please check your credentials.")