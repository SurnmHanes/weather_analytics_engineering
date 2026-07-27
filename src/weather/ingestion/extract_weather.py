import requests
from src.weather.transformation.transform_weather import create_weather_dataframe
from src.weather.transformation.validate_weather import validate_weather
from src.weather.config import LATITUDE, LONGITUDE, START_DATE, END_DATE, HOURLY_VARIABLES

def get_weather():
    
    url="https://archive-api.open-meteo.com/v1/archive"
    
    params = {
    "latitude": LATITUDE,
    "longitude": LONGITUDE,
    "start_date": START_DATE,
    "end_date": END_DATE,
    "hourly": HOURLY_VARIABLES
    }

    response = requests.get(
                    url,
                    params=params
                )

    response.raise_for_status()

    return response.json()