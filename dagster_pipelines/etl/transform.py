import pandas as pd
import numpy as np

thai_months = {
    'ม.ค.': '01', 'ก.พ.': '02', 'มี.ค.': '03', 'เม.ย.': '04',
    'พ.ค.': '05', 'มิ.ย.': '06', 'ก.ค.': '07', 'ส.ค.': '08',
    'ก.ย.': '09', 'ต.ค.': '10', 'พ.ย.': '11', 'ธ.ค.': '12'}

def clean_data(frame) -> pd.DataFrame:
    # KPI_PATH=os.path.join(os.getcwd(), "dagster_pipelines/data/KPI_FY.xlsm")
    # df_KPI_data=pd.read_excel(KPI_PATH,sheet_name="Data to DB" ,engine="openpyxl")
    # # plan columns
        
    df=frame.drop(frame.columns[[0,15,17,19,21]],axis=1)

            # df2=df.iloc[:,12:13]

            # print(df2.info())
            # df_re=df2.rename(columns={df2.columns[0]:"transaction_date"})

    df_rename=df.rename(columns={df.columns[0]:'project_id',
                                        df.columns[1]:'project_name',
                                        df.columns[2]:'project_type_name',
                                        df.columns[3]:'dept_name',
                                        df.columns[4]:'dept_sub_name',
                                        df.columns[5]:'purchase_method_name',
                                        df.columns[6]:'purchase_method_group_name',
                                        df.columns[7]:'announce_date',
                                        df.columns[8]:'project_money',
                                        df.columns[9]:'price_build',
                                        df.columns[10]:'sum_price_agree',
                                        df.columns[11]:'budget_year',
                                        df.columns[12]:'transaction_date',
                                        df.columns[13]:'province',
                                        df.columns[14]:'district',
                                        df.columns[15]:'subdistrict',
                                        df.columns[16]:'project_status',
                                        
                                        df.columns[17]:'latitude',
                                        df.columns[18]:'longitude',
                                        df.columns[19]:'winner_tin',
                                        df.columns[20]:'winner',
                                        df.columns[21]:'contract_no',
                                        df.columns[22]:'contract_date',
                                        df.columns[23]:'contract_finish_date',
                                        df.columns[24]:'price_agree',
                                        df.columns[25]:'status',

            





        })
  





    return df_rename


# def transform_date(df: pd.DataFrame) -> pd.DataFrame:
    
#     # Perform transformations on the DataFrame
#     # For example, you can rename columns, filter rows

#     date_pattern = df.str.split(' ', expand=True)
#     date_pattern[1]= date_pattern[1].replace(thai_months, regex=True)
#     date_pattern[2]= date_pattern[2].astype('int')
#     # date_pattern[2]= pd.to_numeric(date_pattern[2], errors='coerce')
#     date_pattern[2]= date_pattern[2].apply(lambda x: int(x+2500)-543 if x< 100 else x)
#     df=pd.to_datetime(date_pattern[0] + '-' + date_pattern[1] + '-' + date_pattern[2].astype(str), format='%d-%m-%Y', errors='coerce')
#     df= df.replace(r'^\D+\s*$', np.nan, regex=True)





#     return df


def transform_date(df: pd.Series) -> pd.Series:
    # แยกวัน เดือน ปี
    df= df.replace(r'^\D+\s*$', np.nan, regex=True)
    date_pattern = df.str.split(' ', expand=True)

    # แปลงเดือนเป็นเลข
    date_pattern[1] = date_pattern[1].replace(thai_months, regex=True)

    # แปลงปี: รองรับ NaN โดยใช้ apply + เช็ค
    def convert_year(x):
        try:
            x = float(x)
            return int(x + 2500) - 543 if x < 100 else int(x)
        except:
            return np.nan

    date_pattern[2] = date_pattern[2].apply(convert_year)

    # รวมวัน-เดือน-ปีเป็น string แล้วแปลงเป็น datetime
    full_date_str = date_pattern[0] + '-' + date_pattern[1] + '-' + date_pattern[2].astype('Int64').astype(str)
    date_series = pd.to_datetime(full_date_str, format='%d-%m-%Y', errors='coerce')

    return date_series