WITH date_range AS (

    SELECT
        MIN( CAST( observation_datetime AS DATE ) ) AS min_date,
        MAX( CAST( observation_datetime AS DATE ) ) AS max_date     
    FROM 
    stg_weather

),
date_base AS (
    SELECT
        unnest AS date_day 
    FROM 
        UNNEST(
            GENERATE_SERIES(
                CAST( (SELECT min_date FROM date_range) AS TIMESTAMP ),
                CAST( (SELECT max_date FROM date_range) AS TIMESTAMP ),
                INTERVAL 1 DAY
            )
        ) AS date_array
)
SELECT
    CAST(strftime(date_day, '%Y%m%d') AS INT64) AS date_key,
    date_day,
    EXTRACT(YEAR FROM date_day) AS YEAR,
    EXTRACT(MONTH FROM date_day) AS MONTH,
    strftime(date_day, '%B') AS month_name,
    EXTRACT(QUARTER FROM date_day) AS QUARTER,
    EXTRACT(DAY FROM date_day) AS day_of_month,
    strftime(date_day, '%A') AS day_name,
    EXTRACT(YEAR FROM date_day) = EXTRACT(YEAR FROM CURRENT_DATE) AS is_current_year
FROM
    date_base