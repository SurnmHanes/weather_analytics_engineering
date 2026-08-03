with source as (
    select 
        datetime,
        temperature,
        precipitation,
        wind_speed,
        location,
        loaded_at
    from {{ source('weather', 'weather_raw') }}
),

renamed as (
    select 
        datetime as observation_datetime,
        temperature as temperature_celsius,
        precipitation as precipitation_mm,
        wind_speed as wind_speed_kmh,
        location,
        loaded_at
    from source
)

select * from renamed