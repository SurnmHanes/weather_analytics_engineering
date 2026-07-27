import pandas as pd

def validate_weather(df: pd.DataFrame):

    print("Checking dataframe is not empty...")
    validate_not_empty(df)

    print("Checking required columns...")
    validate_columns(df)

    print("Checking duplicate timestamps...")
    validate_unique_datetime(df)

    print("Checking for null values...")
    validate_no_nulls(df)

    print("✓ Validation passed.")

def validate_not_empty(df: pd.DataFrame):

    if df.empty:
        raise ValueError("Weather dataframe is empty")

def validate_columns(df: pd.DataFrame):
    expected_columns = [
        "datetime",
        "temperature",
        "precipitation",
        "wind_speed"
    ]

    missing = set(expected_columns) - set(df.columns)

    if missing:
        raise ValueError(f"Missing columns: {missing}")

def validate_unique_datetime(df: pd.DataFrame):

    duplicates = df.duplicated(subset=["datetime"]).sum()

    if duplicates > 0:
        raise ValueError(f"Found {duplicates} duplicate timestamps")

def validate_no_nulls(df: pd.DataFrame):

    null_counts = df.isna().sum()

    if null_counts.any():
        raise ValueError(f"Null values found: \n{null_counts}")

