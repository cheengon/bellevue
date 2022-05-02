#draft weather program
#need to incorporate city input
#need to be able to run multiple times
#add comments
#validation still needed

import requests

def main():
    APP_ID = "ee682d591d365ef3094228a13400017f"
    # get zip code from user
    zip_code = input("Enter a 5-digit, US zip code: ").strip()
    # &units=imperial ensures degrees Farenheit and miles per hour
    url = f"https://api.openweathermap.org/data/2.5/weather?zip={zip_code},us&APPId={APP_ID}&units=imperial"
    weather_data = get_weather_json(url)
    display_results(weather_data)

def from_utc_to_local_hour(utc_timestamp, shift):
    utc_datetime = datetime.utcfromtimestamp(utc_timestamp + shift)
    hour_min_24 = utc_datetime.strftime("%H:%M")
    hour_min_12 = datetime.strptime(hour_min_24, "%H:%M")
    return hour_min_12.strftime("%I:%M %p")

def get_weather_json(url):
    resp = requests.get(url)
    data = resp.json()
    return data 

def display_results(weath_dict):
    print(f"The weather info for {weath_dict['name']} is:")
    print(f"\n\t- {get_conditions(weath_dict).capitalize()}")
    print(f"\t- The temperature is {get_temperature(weath_dict)} degrees Farenheit") 
    
def get_conditions(weather_dict):
    return weather_dict["weather"][0]["description"]

def get_temperature(weather_dict):
    return weather_dict["main"]["temp"]

if __name__ == "__main__":
    main()