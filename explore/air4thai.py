import requests
import json

url = "http://air4thai.pcd.go.th/services/getNewAQI_JSON.php"
resp = requests.get(url, timeout=30, verify=False)

print("Status:", resp.status_code)
data = resp.json()

print("Keys ชั้นนอก:", list(data.keys()))
stations = data["stations"]
print("จำนวนสถานี:", len(stations))

print(json.dumps(stations[0], ensure_ascii=False, indent=2))