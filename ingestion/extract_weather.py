import requests

def get_weather():
    
    url="https://archive-api.open-meteo.com/v1/archive"
    
    params = {
    "latitude": 52.72,
    "longitude": -1.37,
    "start_date": "2010-01-01",
    "end_date": "2026-06-30",
    "hourly": [
        "temperature_2m",
        "precipitation",
        "wind_speed_10m"
        ]
    }

    response = requests.get(
                    url,
                    params=params
                )

    response.raise_for_status()

    return response.json()

if __name__ == "__main__":

    weather = get_weather()

    print(weather['hourly'].keys())
