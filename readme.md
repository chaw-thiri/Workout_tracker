# Exercise Tracker 
* This program helps you record your daily exercises in the Google sheet by recalculating the energy expenditure from the category and duration of your exercise.
* ![image](https://github.com/chaw-thiri/Workout_tracker/assets/113085742/89b1b968-12be-41c9-b99e-3fe3fb23a187)
* Using the Nutritionix API from Syndigo University and Sheety API, the Python program and the Google sheet are permanently connected so that every record you make in this program will be saved in the Google sheet.
  
![image](https://github.com/chaw-thiri/Workout_tracker/assets/113085742/d3297cce-900e-4953-97ff-8e7b6aca8dc2)

## Setup
### Environment Variables
Before running the script, make sure to set the following environment variables:

app_id: Your Nutritionix API App ID.
api_key: Your Nutritionix API Key.


## Dependencies
```pip install requests```
## Usage
Run the script (main.py).
When prompted, enter details about your workout.
The script will make a request to the Nutritionix API to get exercise data based on your input.
The retrieved workout data will be stored in a spreadsheet using the Sheety API.
## Additional Notes
It is mandatory to have active internet connection while running the script as it relies on external APIs.
