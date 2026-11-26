import os
from datetime import datetime, timezone
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()
OUT = Path("explore/samples")
OUT.mkdir(parents=True, exist_ok=True)
TS = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") 

def save(name:str, content: bytes, ext: str) -> None:
    path = OUT / f"{name}_{TS}.{ext}"
    path.write_bytes(content)
    print(f"saved {path} ({len(content):,} Bytes")
    
# 1) Open Meteo
r = requests.get(
    "https://api.open-meteo.com/v1/forecast",
    params = {
    "latitude": 13.73,
    "longitude": 100.78,
    "hourly": "temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m,wind_direction_10m",
    "past_days": 2,
    "forecast_days": 1,
    "timezone": "UTC",
    },
    timeout=30,
)
r.raise_for_status()
save("open_meteo", r.content, "json")

# 2) Air4Thai
r =requests.get(
    "http://air4thai.pcd.go.th/services/getNewAQI_JSON.php",
    timeout=30,
    verify=False
)
r.raise_for_status()
save("air4thai", r.content, "json")

# 3) FIRMs
key = os.getenv("FIRMS_MAP_KEY")
if key:
    r = requests.get(
        f"https://firms.modaps.eosdis.nasa.gov/api/country/csv/{key}/VIIRS_SNPP_NRT/THA/3",
        timeout=30,
    )
    r.raise_for_status()
    save("firm", r.content, "csv")

else:
    print("API KEY Have an error")
