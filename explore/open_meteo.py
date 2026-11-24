import requests
import pandas as pd 

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 13.73,
    "longitude": 100.78,
    "hourly": "temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m,wind_direction_10m",
    "past_days": 2,
    "forecast_days": 1,
    "timezone": "UTC",
}


resp = requests.get(url, params=params, timeout=30)
print("Status:", resp.status_code)
data = resp.json()

print("Keys Outside:", list(data.keys()))
print("หน่วย:", data["hourly_units"])

df = pd.DataFrame(data["hourly"])
print(df.head())
print("จำนวนแถว:", len(df))
print(df.isna().sum())