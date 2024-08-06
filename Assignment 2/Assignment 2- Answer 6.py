# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1g44QWDyCQ-IgokSMfoUKvkSmJC_WhO2m
"""

import requests
import pandas as pd
import time
from datetime import datetime

url = "http://api.open-notify.org/iss-now.json"
header = {
    "User-Agent":"Nasa"
}

data_list = []
num_records = 100
while len(data_list) < num_records:
    try:
        response = requests.get(url,headers=header, timeout=10)
        response.raise_for_status()
        json_data = response.json()
        timestamp = json_data["timestamp"]
        latitude = json_data["iss_position"]["latitude"]
        longitude = json_data["iss_position"]["longitude"]
        data_list.append({
            "Timestamp": timestamp,
            "Latitude": latitude,
            "Longitude": longitude
        })
        time.sleep(2)
    except requests.exceptions.Timeout:
        print("Connection timed out. Retrying...")
        time.sleep(5)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        break

df = pd.DataFrame(data_list)
csv= "iss_data.csv"
df.to_csv(csv, index=False)
print(pd.read_csv(csv))



