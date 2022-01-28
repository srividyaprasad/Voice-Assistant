import requests
import json
import speech_rec as s
import text_to_speech as t
def main(city, country):
    url = "http://api.weatherbit.io/v2.0/current"

    querystring = {"city":city, "country": country, "key": "ca8bbc0aa955422ba8a9f3fe3c82956a"}
    response = requests.request("GET", url, params=querystring)

    line = json.loads(response.text)

    desc = str(line['data'][0]['weather']['description'])
    temp = str(line['data'][0]['temp'])
    windspd = str(line['data'][0]['wind_spd'])
    precip = str(line['data'][0]['precip'])
    t.speak("Description")
    t.speak(desc) 
    t.speak("Temperature")
    t.speak(temp)
    t.speak("Wind speed")
    t.speak(windspd)
    t.speak("Precipitation")
    t.speak(precip)
