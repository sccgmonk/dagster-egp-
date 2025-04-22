import pandas as pd
import numpy as np
import glob
import os
PATH="dagster_pipelines/data/"
M_CENTER_PATH="dagster_pipelines/data/M_Center.csv"


# 2.1.1 Read KPI evaluation data from the "Data to DB" sheet in the "KPI_FY.xlsm" Excel file
def read_excel(path: str = PATH, sheet_name: str = "Data to DB") -> pd.DataFrame:
    all_files = glob.glob(os.path.join(path, '*.csv'))
    if not all_files:
        raise ValueError("ไม่พบไฟล์ CSV")

    df_list = [pd.read_csv(f) for f in all_files]
    frame = pd.concat(df_list, ignore_index=True)
    
    # Push raw data to XCom as JSON string

    return frame
    


