from dagster import get_dagster_logger
import duckdb
import pandas as pd

logger = get_dagster_logger()

def load_to_duckdb(df: pd.DataFrame, table_name: str) -> None:
    try:
        with duckdb.connect("/opt/dagster/app/dagster_pipelines/db/db_grp.db") as con:
       
            logger.info("Connected to DuckDB successfully.")
            
            con.sql("CREATE SCHEMA IF NOT EXISTS db_grp;")
            con.register('df_view', df)
            
            con.sql(f"CREATE OR REPLACE TABLE db_grp.main.{table_name} AS SELECT * FROM df;")
            result = con.sql(f"SELECT * FROM db_grp.main.{table_name} LIMIT 1").fetchone()
            logger.info(f"Sample record from {table_name}: {result}")
            logger.info(f"Data successfully inserted into table '{table_name}'.")
    except Exception as e:
        logger.error(f"Error loading data into DuckDB: {e}")
        raise