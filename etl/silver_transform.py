from sqlalchemy import text
from db_connection import get_engine

def transform_silver():
    engine = get_engine()

    sql = """
    DROP TABLE IF EXISTS silver.sales;

    CREATE TABLE silver.sales AS
    SELECT
        order_id,
        user_id,
        product,
        price * quantity AS total_price,
        DATE(order_date) AS order_date
    FROM bronze.transactions;
    """

    with engine.begin() as conn:
        conn.execute(text(sql))

    print("SILVER transform completed")

if __name__ == "__main__":
    transform_silver()
