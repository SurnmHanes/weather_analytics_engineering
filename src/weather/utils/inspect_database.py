import duckdb

conn = duckdb.connect("weather.duckdb")

tables = conn.execute( "SHOW TABLES").fetchall()

print(tables)

result = conn.execute(""" SELECT * FROM weather_raw LIMIT 10 """).fetchdf()
validation = conn.execute(""" SELECT COUNT(*) AS rows, MIN(datetime), MAX(datetime) FROM weather_raw """).fetchdf()

print(result)
print(validation)
conn.close()
