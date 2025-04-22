import dagster as dg
import duckdb


from dagster_pipelines.etl.extract import read_excel
from dagster_pipelines.etl.transform import clean_data,transform_date
from dagster_pipelines.etl.load import load_to_duckdb




@dg.asset(compute_kind="duckdb", group_name="plan1")
def egp_data(context: dg.AssetExecutionContext):
    context.log.info("Reading KPI Excel file...")
    df_raw = read_excel()
    context.log.info("Pivoting KPI data...")
    df= clean_data(df_raw)
    context.log.info("Saving egp_data")

    # context.log.info("Loading pivoted KPI data into DuckDB table: KPI_FY")
    # load_to_duckdb(df, "KPI_FY")
    return df

@dg.asset(compute_kind="duckdb", group_name="plan1")
        #   ,deps=[ego_data])
def Transform_date(context: dg.AssetExecutionContext,egp_data):
    context.log.info("Transforming date columns...")
    df = egp_data
    # tranform announce_date
    
    df['announce_date']=transform_date(df['announce_date'])
    context.log.info(f"Preview announce_date raw: {df['announce_date'].dropna().unique()[:5]}")
    # tranform transaction_date
    df['transaction_date']=transform_date(df['transaction_date'])
    context.log.info(f"Preview transaction_date raw: {df['transaction_date'].dropna().unique()[:5]}")
    # tranform contract_date
    df['contract_date']=transform_date(df['contract_date'])
    context.log.info(f"Preview contract_date raw: {df['contract_date'].dropna().unique()[:5]}")
    # tranform contract_finish_date
    df['contract_finish_date']=transform_date(df['contract_finish_date'])
    context.log.info(f"Preview contract_finish_date raw: {df['contract_finish_date'].dropna().unique()[:5]}")
    # tranform project_money
        # ตรวจสอบ missing

    # รองรับ latitude/longitude
    df['project_id'].astype(str)
    df['latitude'].astype(float)
    df['longitude'].astype(float)
    # df['longitude'] = pd.to_numeric(df.get('longitude'), errors='coerce')

    context.log.info(f"Missing latitude: {df['latitude'].isnull().sum()}")
    context.log.info(f"Missing longitude: {df['longitude'].isnull().sum()}")

    context.log.info("Loading transformed egp data into DuckDB table: egp_data")
    load_to_duckdb(df, "egp_data")
 
   

    return df
   

# # 2.3.1.2 Load M_Center.csv into M_Center
# @dg.asset(compute_kind="duckdb", group_name="plan1")
# def m_center(context: dg.AssetExecutionContext):
#     context.log.info("Reading M_Center CSV...")
#     df = read_csv()
#     context.log.info("Loading M_Center data into DuckDB table: M_Center")
#     load_to_duckdb(df, "M_Center")
#     return df

# # 2.3.2 Create asset kpi_fy_final_asset()
# @dg.asset(
#            compute_kind="duckdb", 
#            group_name="plan1",
#            deps=[kpi_fy,m_center],
#            )



# def kpi_fy_final_asset(context: dg.AssetExecutionContext):
#     context.log.info("Joining KPI_FY and M_Center tables...")
#     con = duckdb.connect("/opt/dagster/app/dagster_pipelines/db/plan.db")
#     df_joined = con.execute("""
#         SELECT
#             k.*,
#             m.Center_Name,
#             CURRENT_TIMESTAMP AS updated_at
#         FROM plan.plan.KPI_FY k
#         LEFT JOIN plan.plan.M_Center m
#         ON k.Center_ID = m.Center_ID
#     """).df()
#     con.close()
    # conn = duckdb.connect("dagster_pipelines/db/plan.db", read_only=True)
    # conn.execute("CREATE SCHEMA IF NOT EXISTS plan;")
    # context.log.info("Loading final joined data into DuckDB table: KPI_FY_Final")
    # load_to_duckdb(df_joined, "KPI_FY_Final")
    # return df_joined


    # df = conn.execute("""
    #     SELECT k.*, m.Center_Name, CURRENT_TIMESTAMP AS updated_at
    #     FROM KPI_FY k
    #     LEFT JOIN M_Center m
    #     ON k.Center_ID = m.Center_ID
    # """).fetchdf()

    # load_to_duckdb(df, "KPI_FY_Final")

   