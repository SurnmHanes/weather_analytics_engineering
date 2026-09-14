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
    EXTRACT(YEAR FROM date_day) AS Year,
    EXTRACT(MONTH FROM date_day) AS Month,
    MONTHNAME(date_day) AS month_name,
    strftime(date_day, '%b') AS short_month_name,
    strftime(date_day, '%b %Y') AS month_year,
    CAST(strftime(date_day, '%Y%m') AS INT64) AS month_year_sort,
    EXTRACT(DAY FROM date_day) AS day_of_month,
    strftime(date_day, '%A') AS day_name,
    EXTRACT(YEAR FROM date_day) = EXTRACT(YEAR FROM CURRENT_DATE) AS is_current_year
FROM
    date_base