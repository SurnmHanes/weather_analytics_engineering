import pandas as pd

def create_weather_dataframe(weather):
    df = pd.DataFrame(
        {
            "datetime": weather['hourly']['time'],
            "temperature": weather['hourly']['temperature_2m'],
            "precipitation": weather['hourly']['precipitation'],
            "wind_speed": weather['hourly']['wind_speed_10m']
        }
    )

    return df