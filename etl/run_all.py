from ingest_raw import ingest_raw
from bronze_transform import transform_bronze
from silver_transform import transform_silver
from gold_transform import transform_gold

def run_pipeline():
    print("=== PIPELINE STARTED ===")

    ingest_raw()
    transform_bronze()
    transform_silver()
    transform_gold()

    print("=== PIPELINE COMPLETED SUCCESSFULLY ===")

if __name__ == "__main__":
    run_pipeline()
