import requests
from twilio.rest import Client
import os

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
api_key = os.environ.get("OWN_API_KEY")


MY_LAT = 0.000
MY_LONG = -0.000

FROM_NUMBER = "+13397778888"
MY_NUMBER = "+16473334567"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()
all_day_weather = weather_data["list"]
next_twelve_hour_conditions = []
for x in all_day_weather:
    forecast = x["weather"]
    condition_id = forecast[0]["id"]
    condition = forecast[0]["main"]
    next_twelve_hour_conditions.append(condition_id)

if any(800 <= value < 900 for value in next_twelve_hour_conditions):
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It will be quite cloudy tomorrow. Be sure to take your umbrella ☁️☂️.",
        from_= FROM_NUMBER,
        to= MY_NUMBER,
    )

    print(message.sid, message.status, message.body)


