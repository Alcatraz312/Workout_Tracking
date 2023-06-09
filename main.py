import requests
import datetime
from keys import *

exercise = input()

api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id" : APP_ID,
    "x-app_key" : API_KEY
}

params = {
    "query" : exercise,
    "gender" : "male",
    "weight_kg" : "60",
    "height_cm" : "182.88",
    "age" : "18"
    
}

response = requests.post(api_endpoint, json=params, headers=headers)
result = response.json()


