import duckdb

conn = duckdb.connect("weather.duckdb")

tables = conn.execute( "SHOW TABLES").fetchall()

print(tables)

result = conn.execute(""" SELECT * FROM weather_raw LIMIT 10 """).fetchdf()
validation = conn.execute(""" SELECT COUNT(*) AS rows, MIN(datetime), MAX(datetime) FROM weather_raw """).fetchdf()

latest_observations = conn.execute(""" SELECT * FROM fact_weather ORDER BY observation_datetime DESC LIMIT 50 """).fetchdf()   

number_of_observations = conn.execute(""" SELECT COUNT(*) AS rows FROM fact_weather """).fetchdf()

grain_check = conn.execute(""" SELECT observation_datetime, COUNT(*) AS rows FROM fact_weather GROUP BY observation_datetime HAVING COUNT(*) > 1 ORDER BY observation_datetime DESC """).fetchdf()

print("weather raw:", result)
print("validation:", validation)
print("latest observations:", latest_observations)
print("number of observations:", number_of_observations)
print("grain check:", grain_check)
conn.close()
