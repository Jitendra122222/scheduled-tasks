import requests
import os
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
  "lat": "43.343777",
  "lon": "-0.127758",
  "appid": api_key,
  "cnt": 4,
}
response = requests.get(OWM_Endpoint, params=weather_params)
weather_data = response.json()
will_snow = False
for hour_data in weather_data["list"]:
  condition_code = hour_data["weather"][0]["id"]
  if int(condition_code) < 900:
    will_snow = True

if will_snow:
  client = Client(account_sid, auth_token)
  print(client)
  try:
    message = client.messages.create(
      from_="whatsapp:+14155238886",
      body="It's going to rain today. Remember to bring an umbrella",
      to="whatsapp:+918208134214"
    )
    print(message.body)
  except Exception as e:
    print("Failed to send WhatsApp message:", e)
else:
  print("No snow expected in the next forecast window.")
