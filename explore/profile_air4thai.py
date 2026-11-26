import glob
import json

import pandas as pd 

path = sorted(glob.glob("explore/samples/air4thai_*.json"))[-1]
with open(path, encoding="utf-8") as f:
    data = json.load(f)
    
df = pd.json_normalize(data["stations"])  
print("จำนวนสถานี:", len(df))
print("คอลัมน์:", df.columns.tolist())

# เปลี่ยนชื่อคอลัมน์ตรงนี้ให้ตรงกับที่ print ออกมา
pm_col = "AQILast.PM25.value"
pm_raw = df[pm_col]
print("\nชนิดข้อมูลดิบ:", pm_raw.dtype)
print("ค่าที่พบบ่อย:\n", pm_raw.value_counts().head(100))

pm = pd.to_numeric(pm_raw, errors="coerce")
print("\nแปลงเป็นตัวเลขไม่ได้:", pm.isna().sum())
print("ค่าติดลบ:", (pm < 0).sum())
print(pm[pm >= 0].describe())

print("\nวัน-เวลาที่พบ:")
print(df[["AQILast.date", "AQILast.time"]].value_counts().head())

print("\nstationID ซ้ำไหม:", df["stationID"].duplicated().any())