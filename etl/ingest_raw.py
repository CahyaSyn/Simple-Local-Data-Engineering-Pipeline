import pandas as pd
from db_connection import get_engine

def ingest_raw():
    engine = get_engine()

    df = pd.read_csv("data/transactions_raw.csv")

    df.to_sql(
        name="transactions_raw",
        con=engine,
        schema="raw",
        if_exists="replace",
        index=False
    )

    print("RAW ingestion completed")

if __name__ == "__main__":
    ingest_raw()
