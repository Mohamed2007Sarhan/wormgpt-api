import sqlite3
import datetime
import pytz
import requests
import sys
from time import sleep

def api_openai(api):
    api_openai_api = api
    return api_openai_api

def Wormgpt(api_openai_api):
    worm = '''\033[0;31m
     __      __                                      __    
    /  \    /  \___________  _____      ____ _______/  |_  
    \   \/\/   /  _ \_  __ \/     \    / ___\\____ \   __\ 
     \        (  <_> )  | \/  Y Y  \  / /_/  >  |_> >  |   
      \__/\  / \____/|__|  |__|_|  /  \___  /|   __/|__|   
           \/                    \/  /_____/ |__|
           
           𝙱𝚢 : @F_E_R_X
    '''
    for wo in worm.splitlines():
        print(wo)
        sleep(0.05)

    end_datetime = datetime.datetime(2024, 1, 30, 0, 0, 0)  # Set the end time
    egypt_timezone = pytz.timezone("Africa/Cairo")

    remaining_time = end_datetime.astimezone(egypt_timezone) - datetime.datetime.now(egypt_timezone)

    if datetime.datetime.now(egypt_timezone) >= end_datetime.astimezone(egypt_timezone):
        print("[!] The Specified Time Has Expired")
        exit(0)

    while True:
        url = "https://dev-gpts.pantheonsite.io/wp-admin/js/apis/WormGPT.php"
        Ch = input('\n\033[0;37m[\033[0;31m Worm gpt \033[0;37m] :~# \033[0;37m')
        if Ch == 'exit':
            print("Thanks for using")
            print("\033[91mUnder the auspices of the Black Crow\033[0m")
            exit(0)
            
        data = {
            "text": Ch,
            "api_key": api_openai_api,
            "temperature": 0.9
        }

        response = requests.post(url, json=data).json()

        text = response["choices"][0]["message"]["content"]

        for i in text:
            sys.stdout.write(str(i))
            sys.stdout.flush()
            sleep(0.005)

def check_user(username, password):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM table_name WHERE api_worm_gpt_db=? AND pass=?", (username, password))
    user_data = cursor.fetchone()

    conn.close()

    return user_data

def execute_admin_code():
    print("hello")

# Get username and password input
def login(username, password):
    username_input = username
    password_input = password

    # Validate user credentials
    user_data = check_user(username_input, password_input)

    if user_data:
        print("Good")

        if user_data[1] == 'admin' and user_data[2] == 'admin_pass':
            execute_admin_code()
    else:
        print("Error")



