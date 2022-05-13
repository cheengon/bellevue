"""
This program is the final project for my Intro to Programming class and will 
provide you the weather forecast based on a city or zip code inputted by the user
"""
# Import required modules
import requests
from datetime import datetime

# Welcome message
welcome=("Hello, this program will provide you the weather forecast based on city or zip code.")
print(welcome)
print("")
input("Press Enter to continue...")
print("")

# Main function which asks for user input to specity search by city or zip code
def main():
    while True:
        answer = input("To get weather information enter 'C' for city or 'Z' for zip code. ") 
        if answer == "C" or answer == "c":
            try:
                if_city()

            except Exception:
                print("That didn't work. Please try again.")
                if_city()
                
        if answer == "Z" or answer == "z":
            try:
                if_zip()

            except Exception:
                print("That didn't work. Please try again.")
                if_zip()
        else: 
            print("This is not supported at this time. Please try again.")

# Function if user input is a zip code
def if_zip():
    API = "ee682d591d365ef3094228a13400017f"
    # get zip code from user
    zip_code = input("Enter a 5-digit, US zip code: ").strip()
    # units=imperial provides degrees is Fahrenheit
    url = f"https://api.openweathermap.org/data/2.5/weather?zip={zip_code},us&APPID={API}&units=imperial"
    weather_data = get_weather_json(url)
    display_results(weather_data)

# Question to allow user to run program multiple times
    newSearch = input("\nDo you want to perform a new search? Type Yes or No: ")
    if newSearch == "Yes" or newSearch == "yes" or newSearch == "y" or newSearch == "Y":
        main()
    if newSearch == "No" or newSearch == "no" or newSearch == "n" or newSearch == "N":
        exit()

# Function if user input is a city
def if_city():
    API = "ee682d591d365ef3094228a13400017f"
    # get zip code from user
    city = input("Enter a U.S. City: ").strip()
    # units=imperial provides degrees is Fahrenheit
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},us&APPID={API}&units=imperial"
    weather_data = get_weather_json(url)
    display_results(weather_data)

# Question to allow user to run program multiple times
    newSearch = input("\nDo you want to perform a new search? Type Yes or No: ")
    if newSearch == "Yes" or newSearch == "yes" or newSearch == "y" or newSearch == "Y":
        main()
    if newSearch == "No" or newSearch == "no" or newSearch == "n" or newSearch == "N":
        exit()

# Function converts time from UTC to Local Time
def from_utc_to_local_hour(utc_timestamp, shift):
    utc_datetime = datetime.utcfromtimestamp(utc_timestamp + shift)
    hour_min_24 = utc_datetime.strftime("%H:%M")
    hour_min_12 = datetime.strptime(hour_min_24, "%H:%M")
    return hour_min_12.strftime("%I:%M %p")

# Function to parse JSON data from openweather API for weather information requested
def get_weather_json(url):
    resp = requests.get(url)
    data = resp.json()
    return data 

# Function prints weather information outputs
def display_results(weath_info):
    print(f"\nThe weather information for {weath_info['name']} is:")
    print(f"\nCurrent temperature: {get_temperature(weath_info)} degrees Fahrenheit") 
    print(f"Maximum temperature: {get_temp_max(weath_info)} degrees Fahrenheit")
    print(f"Minimum temperature: {get_temp_min(weath_info)} degrees Fahrenheit")
    print(f"Current conditions: {get_conditions(weath_info).capitalize()}")
    print(f"Feels like: {get_feels_like(weath_info)} degrees Fahrenheit") 
    print(f"Sunrise: {get_sunrise(weath_info)}") 
    print(f"Sunset: {get_sunset(weath_info)}") 
    
# Function provides current weather conditions    
def get_conditions(weather_info):
    return weather_info["weather"][0]["description"]

# Function provided current temperature
def get_temperature(weather_info):
    return weather_info["main"]["temp"]

# Function provides what the weather feels like
def get_feels_like(weather_info):
    return weather_info["main"]["feels_like"]

# Function provides what the minimum temperature
def get_temp_min(weather_info):
    return weather_info["main"]["temp_min"]

# Function provides what the maximum temperature
def get_temp_max(weather_info):
    return weather_info["main"]["temp_max"]

# Function provides sunrise time
def get_sunrise(weather_info):
    return from_utc_to_local_hour(weather_info["sys"]["sunrise"], weather_info["timezone"])

# Function provides sunset time
def get_sunset(weather_info):
    return from_utc_to_local_hour(weather_info["sys"]["sunset"], weather_info["timezone"])

main()
