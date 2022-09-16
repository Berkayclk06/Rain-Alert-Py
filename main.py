import requests
from twilio.rest import Client
import os

API_KEY = os.environ["API_KEY"]
account_sid = os.environ["ACC_SID"]
auth_token = os.environ["AUTH_TOKEN"]

MY_LAT = os.environ["MY_LAT"]
MY_LON = os.environ["MY_LON"]

parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "exclude": "current,minutely,daily",
    "appid": API_KEY,
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_date = response.json()

will_rain = False

for i in range(12):
    weather_id = weather_date["hourly"][i]["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True
        break

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body="It looks like it's going to rain. Bring an umbrella ☔",
            from_=os.environ["FROM_PHONE"],
            to=os.environ["TO_PHONE"]
        )
