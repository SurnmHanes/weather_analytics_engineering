import duckdb
from datetime import datetime, timezone

def load_weather(df):
    load_timestamp = datetime.now(timezone.utc)

    df['loaded_at'] = load_timestamp

    conn = duckdb.connect("weather.duckdb")

    conn.execute(""" DROP TABLE IF EXISTS weather_raw """)
    conn.execute(""" CREATE TABLE weather_raw AS SELECT * FROM df """)

    conn.close()