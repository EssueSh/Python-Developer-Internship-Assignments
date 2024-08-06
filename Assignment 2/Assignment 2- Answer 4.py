#!/usr/bin/env python
# coding: utf-8

# In[5]:


import requests
import json
url = "http://api.open-notify.org/iss-now.json"
header = {
    "User-Agent":"python-requests/2.28.1"
}

data = requests.get(url)
print(data)
json_data = json.loads(data.text)
print(json_data)


# In[ ]:




