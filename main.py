# ------------- Constants ----------------
from datetime import datetime
import os
import requests


# For nutritionix
# --------------------------------------------- Environment Variables for App_id and
App_id = os.environ.get("app_id")
os.environ["app_id"] = "d66d5c91"
App_Id = os.environ.get("app_id", "Not Exist")
os.environ["api_key"] = "25b1cab14bfb5167ea3d74538f46a41d"
API_key = os.environ.get("api_key")
API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
# Sheety api
SHEETY_ENDPOINT = "https://api.sheety.co/96fb1b13cf975a5084bce1be82fc3211/workout/workouts"

headers = {
    "x-app-id": App_Id,
    "x-app-key": API_key,
}

parameters = {
    "query": input("Workout :"),
    "weight_kg": 75,
    "height_cm": 166.7,
    "age": 24
}

response = requests.post(API_ENDPOINT, json=parameters, headers=headers)
result = response.json()

# ----------------------- sheety api -----------------------
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
# ---------------------------- adding authentication for the sheet
bearer_header = {
"Authorization":"Bearer dffgeredfwwertsgfdbc2343tet453gfgd435g343gdfh46nyfgtrirtjrjkltrlktgkdr"
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

    sheet_response = requests.post(SHEETY_ENDPOINT, headers=bearer_header,json=sheet_inputs)

    print(sheet_response.text)



