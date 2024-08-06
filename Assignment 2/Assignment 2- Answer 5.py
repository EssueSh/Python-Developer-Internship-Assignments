#!/usr/bin/env python
# coding: utf-8

# In[6]:


import requests
import json
url = "http://api.open-notify.org/iss-now.json"
header = {
    "User-Agent":"python-requests/2.28.1"
}

data = requests.get(url)
print(data)
json_data = json.loads(data.text)
timestamp = json_data["timestamp"]
latitude = json_data["iss_position"]["latitude"]
longitude = json_data["iss_position"]["longitude"]
print('Latitude:',latitude,',','Longitude:',longitude,',','Timestamp:',timestamp)


# In[ ]:




