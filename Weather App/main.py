import requests
import json
city = input("Enter a city name: ")
apiUrl = "https://api.openweathermap.org/data/2.5/weather?units=metric&q="
apiKey = "8a53f49685352c838ca473be11e7eb1f"
reqdata= requests.get(f"{apiUrl}{city}&appid={apiKey}")
reqDic = json.loads(reqdata.text)
data = reqDic["main"]["temp"]
print(f'Current weather at {city} is {data}\u00B0C')

