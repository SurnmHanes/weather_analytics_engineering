import duckdb

def load_weather(df):

    conn = duckdb.connect("weather.duckdb")

    conn.execute(""" CREATE TABLE weather_hourly AS SELECT * FROM df """)

    conn.close()