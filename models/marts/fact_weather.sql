SELECT 
        {{ dbt_utils.generate_surrogate_key(['stg.observation_datetime', 'stg.location']) }} AS observation_key,
        d.date_key,
        l.location_key,
        stg.observation_datetime,
        stg.temperature_celsius,
        stg.precipitation_mm,
        stg.wind_speed_kmh
FROM 
    {{ ref('stg_weather') }} AS stg
INNER JOIN  
    {{ ref('dim_date') }} AS d
ON 
    CAST(stg.observation_datetime AS DATE) = d.date_day
INNER JOIN  
    {{ ref('dim_location') }} AS l
ON 
    stg.location = l.location