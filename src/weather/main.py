from src.weather.ingestion.extract_weather import get_weather
from src.weather.transformation.transform_weather import create_weather_dataframe
from src.weather.transformation.validate_weather import validate_weather
from src.weather.loading.load_duckdb import load_weather

def main():

    print("Starting weather pipeline")

    weather = get_weather()
    print("API weather data obtained")

    df = create_weather_dataframe(weather)
    print("JSON data converted into dataframe")

    validate_weather(df)
    print("dataframe validated")

    load_weather(df)
    print("data loaded to database")
    print("")
    print("Pipeline complete")

if __name__ == "__main__":
    main()