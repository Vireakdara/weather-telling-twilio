import requests
import os
from twilio.rest import Client

api_key = "72d8a7df3d2cfa42e98082f3e3d5b5dd"
city = "Phnom Penh"
lat = "11.556374"
lon = "104.928207"
account_sid = "AC1a2e3805a4c6aee7de25f314bdf8db03"
auth_token = "a01b37b1074c2dbd0e2f520ef677051b"

weather_params = {
    "lat": lat,
    "lon": lon,
    "exclude": "current,minutely,daily",
    "appid": api_key
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=weather_params)
weather_data = response.json()
print(response.status_code)

# Angela's Style
# print(weather_data["hourly"][:12])
weather_slice = weather_data["hourly"][:12]
will_rain = False
for hour_data in weather_slice:
    # print(hour_data["weather"][0]["id"])
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella ☂️☂️☂️",
        from_="+18507249985",
        to="+855963507654"
    )
    print(message.status)

# Dara's Style
# for arr in range(0, 12):
#     condition_code = weather_data["hourly"][arr]["weather"][0]["id"]
#     if condition_code < 700:
#         print("Bring an umbrella")
#     else:
#         print("An umbrella is not need")
