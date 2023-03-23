import requests
import os
from twilio.rest import Client
#$TWILIO_AUTH_TOKEN

END_POINT = "https://api.openweathermap.org/data/2.5/weather" #?lat={lat}&lon={lon}&exclude={part}&appid={API key}
#api_key = "881d1bb0308c6991f40b1efc5e6319a2"

api_key = os.environ.get("OWM_API_KEY")

weather_parameter = {
    "lat": 37.24,
    "lon": 127.05,
    "appid": api_key,
    # step1. use "exclude" keyword - current,minutely,daily
    "exclude": "current,minutely,daily"
}

response = requests.get(END_POINT, params=weather_parameter)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for weather in weather_data["weather"]:
    code = weather["id"]
    if int(code) > 700:
        print(code)  # rain...
        #will_rain = True

if will_rain:

    # Set environment variables for your credentials
    # Read more at http://twil.io/secure
    account_sid = "AC7ad19748cb7e60da08c1f8aa5ecfc639"
    auth_token = "b808a1a7190eb775f1031adeead5e85c"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
      body="Hello from Twilio Bring an umbrella",
      from_="+15076688948",
      to="+821034812939"
    )
    print(message.sid)