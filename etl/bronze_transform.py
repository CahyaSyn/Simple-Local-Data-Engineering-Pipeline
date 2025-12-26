from sqlalchemy import text
from db_connection import get_engine

def transform_bronze():
    engine = get_engine()

    sql = """
    DROP TABLE IF EXISTS bronze.transactions;

    CREATE TABLE bronze.transactions AS
    SELECT DISTINCT
        order_id::INT,
        user_id::INT,
        product,
        price::NUMERIC,
        quantity::INT,
        order_date::TIMESTAMP
    FROM raw.transactions_raw
    WHERE order_id IS NOT NULL;
    """

    with engine.begin() as conn:
        conn.execute(text(sql))

    print("BRONZE transform completed")

if __name__ == "__main__":
    transform_bronze()
