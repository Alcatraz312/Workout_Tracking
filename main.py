import requests
import datetime
import json
from keys import *

exercise = input()

api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id" : APP_ID,
    "x-app_key" : API_KEY
}

params = {
    "query" : exercise,
    

}
