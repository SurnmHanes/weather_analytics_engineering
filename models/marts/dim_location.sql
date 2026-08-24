WITH base AS (
    SELECT
        DISTINCT location
    FROM 
        {{ ref('stg_weather') }}
),
final AS (
    SELECT
        CAST( hash(location) AS INT64) AS location_key,
        location
    FROM
        base        
)

SELECT * FROM final