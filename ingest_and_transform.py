import os
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import requests
import io

# Database connection details from environment variables
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
TABLE_NAME = 'covid19_data'

# URL of the CSV file
CSV_URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'

# Create a database engine
engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.content.decode('utf-8')
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def clean_data(df):
    df.fillna('', inplace=True)
    for column in df.columns[4:]:
        df[column] = pd.to_numeric(df[column], errors='coerce').fillna(0).astype(int)
    return df

def transform_data(df):
    df_melted = df.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], var_name='Date', value_name='Confirmed')
    df_melted['Date'] = pd.to_datetime(df_melted['Date'])
    return df_melted

def ingest_data():
    try:
        data = fetch_data(CSV_URL)
        if data is None:
            return
        
        df = pd.read_csv(io.StringIO(data))
        df = clean_data(df)
        df = transform_data(df)

        df.to_sql(TABLE_NAME, engine, if_exists='replace', index=False)
        print("Data ingested successfully.")
    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
    except pd.errors.EmptyDataError as e:
        print(f"Error: No data - {e}")
    except pd.errors.ParserError as e:
        print(f"Error: Parsing error - {e}")
    except SQLAlchemyError as e:
        print(f"Error: Database error - {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    ingest_data()
