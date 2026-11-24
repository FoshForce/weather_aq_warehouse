import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("FIRMS_MAP_KEY")


url = f"https://firms.modaps.eosdis.nasa.gov/api/area/csv/{key}/VIIRS_SNPP_NRT/97,5,106,21/3"
df = pd.read_csv(url)

print("คอลัมน์:", list(df.columns))
print(df.head())
print("จำนวนจุด:", len(df))
print(df.dtypes)