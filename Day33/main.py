from datetime import datetime
import requests

MY_LAT = 37.566536
MY_LONG = 126.977966

#
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
#
# response.raise_for_status()
#
# data = response.json()
# print(data)
#
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (latitude, longitude)
#
# print(iss_position)
#

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

#endpint ? param = value & ...
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
# split time to get hour
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
time_now = datetime.now()

print(sunrise)
print(sunset)

print(time_now.hour)




