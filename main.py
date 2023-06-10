import requests
from datetime import *
from keys import *

exercise = input("What did you do today : ")

api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/83e215cfe1c28b9eadd13c4a71a27272/myWorkouts/workouts"


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

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

Authorization_header = {
    "Authorization" : f"Bearer {BEARER_TOKEN}"
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheety_endpoint,json=sheet_inputs, headers= Authorization_header)

    print(sheet_response.text)


