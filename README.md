# Analytics Engineering Portfolio Project

## Project Name: Weather Observations

### Overview
This project demonstrates an end-to-end analytics engineering workflow using **Python, dbt and DuckDB**, transforming raw weather observation data from a public API into a structured dimensional model ready for analysis by BI tools.

The pipeline follows a modern layered architecture:<br>
**raw ingestion -> staging -> dimensions -> fact -> BI**

### Objective
Build a reliable, repeatable data pipeline from raw API data to an analytics-ready model, while demonstrating data ingestion, transformation, testing, dimensional modelling and analytical consumption.

### Problem Statement
Weather observations can be obtained from a free API but the raw response is structured for API consumption rather than analytical use. 

How can this data be extracted, validated, transformed and modelled into a consistent analytical structure that supports exploration of weather patterns over time?

### Architecture

#### Data Ingestion
- Raw weather observations obtained via the free **Open-Meteo API**
- Python scripts control the API request, including the observation period and location 
- API JSON responses are converted into tabular **Pandas DataFrames**
- Raw API structures are flattened and transformed into a tabular format suitable for warehouse loading
- Validation is performed before loading to identify unexpected or invalid data
- A <code>loaded_at</code> timestamp is added to identify when each dataset was ingested
- Validated data is loaded into **DuckDB** as the <code>weather_raw</code> source table

The Python ingestion process is separated into discrete responsibilities rather than combining API interrogation, transformation, validation and loading into a single script.

#### Transformation Pipeline (dbt)
The dbt project is structured into 3 layers:

1. Staging Layer
- Renames and standardises raw fields
- Applies appropriate data types
- Derives analytical attributes where appropriate
- Provides a clean interface to raw ingestion layer.

2. Dimension Layer
- Generates a continuous calendar from the observation date range
- Extracts and de-duplicates business entities
- Generates deterministic surrogate keys
- Produces reusable analytical dimensions

3. Fact Layer
- One row per weather observation
- Joins to dimension tables via foreign keys
- Provides the analytical grain from which metrics can be calculated
   
### Data Model

#### Fact Table
- fact_weather
- **Grain**: 1 row per hourly observation

#### Dimensions
- dim_location
- dim_date

### Tech Stack

- DuckDB (data warehouse)
- dbt (data transformation and testing)
- SQL (transformation and analytical logic)
- Python / Pandas (API ingestion and JSON transformation)
- Open-Meteo API (source system)
- GIT + Visual Studio code (development environment)
- Power BI (visualisation layer)

### Data Quality & Testing
Data quality is enforced through a combination of Python validation and dbt tests.

Source-level validation includes:
- validation of observation timestamp, temperature, precipitation and wind speed fields
- <code>not_null</code> tests on key observation and measurement fields

Model-level testing includes:
- <code>not_null</code> tests
- <code>unique</code> tests
- Relationship tests between fact and dimension tables

Documentation is maintained through dbt <code>schema.yml</code> including descriptions of models and key analytical columns.

### Key Engineering Decisions

1. Python for API interrogation.
Separates external API interrogation and JSON transformation from warehouse modelling.

2. Separate configuration from ingestion logic
API parameters and other configurable values are maintained separately from the extraction code.

3. DuckDB as the local analytical warehouse
Lightweight, analytical database well suited for development and portfolio use.

4. dbt for modular transformations
Separates staging, dimension and fact modelling and provides testing and documentation.

5. Separation of raw ingestion from transformation
Raw API data is loaded into DuckDB before being transformed using dbt.

6. Deterministic surrogate keys
Generated using a hash function to provide stable identifiers for dimensional entities.

7. Avoidance of volatile keys
<code>row_number()</code> is not used to generate dimension keys, avoiding changes in key values if the underlying data changes.   

8. Star schema design
Separates dimensional attributes from the weather observation fact table for analytical simplicity.

9. Retention of original observation_timestamp
<code>observation_datetime</code> is retained along with a separate, derived <code>observation_time</code> column allowing both observation-level analysis and time-of-day analysis.

10. Analytical requirements drive the model evolution.
The dimensional model was iteratively enhanced as analytical questions emerged from the Power BI layer.

For example, requirements to analyse observations by calendar month and time of day resulted in the addition of attributes such as <code>month_year</code>, <code>month_year_sort</code> and <code>observation_time</code>

### Analytical Consumption

The resulting dimensional model is consumed by Power BI to demonstrate the warehouse can support different analytical grains and definitions. 

Current analysis includes:

- Daily temperature trends
- Temperature patterns across calendar years
- Monthly and annual precipitation
- Number of precipitation days per year
- Typical wind speed by month
- Maximum recorded wind speed by time of day
- Maximum recorded wind speed by day of week
- Typical wind speed by day of week

The Power BI report is a **consumer of the semantic model rather than the primary focus** of the project.

### Future Improvements

- Add incremental models for large-scale scenarios
- Introduce data freshness tests on ingestion layer
- Complete documentation of the remaining dbt models and columns
- Extend the pipeline to support multiple locations
- Introduce a reusable metrics layer for commonly used KPIs
- Investigate scheduled execution of the ingestion and dbt pipeline
