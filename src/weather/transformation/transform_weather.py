import pandas as pd
from src.weather.config import LOCATION
def create_weather_dataframe(weather):

    hourly = weather['hourly']

    df = pd.DataFrame(
        {
            "datetime": hourly['time'],
            "temperature": hourly['temperature_2m'],
            "precipitation": hourly['precipitation'],
            "wind_speed": hourly['wind_speed_10m']
        }
    )

    df['datetime'] = pd.to_datetime(df['datetime'])
    df['location'] = LOCATION

    return df