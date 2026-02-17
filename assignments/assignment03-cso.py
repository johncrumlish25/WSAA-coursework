# assignment03-cso.py
# This program will retrieve the dataset for the "exchequer account (historical series)" from the CSO
# Author: John Crumlish

import request
import json

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"

response = request.get(url)
return response.json()
