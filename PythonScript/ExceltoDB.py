import pandas as pd
from sqlalchemy import create_engine as ce, text
from datetime import datetime
import SenstiveData
import yagmail
# map excels and DB Tables
file_table_map={
    "Sales_info.xlsx" : "sales_table",
    "Price_info.xlsx" : "price_table"
}

# Map Date columns from tables
date_map={
    "Sales_info.xlsx" : ["Date"],
    "Price_info.xlsx" : ["Date"]
}
data = None
# create a engine to create a connection to Database
engine = ce(f"mysql+mysqlconnector://{SenstiveData.user}:{SenstiveData.password}@{SenstiveData.host}/{SenstiveData.database}")
with engine.begin() as conn:
    for file_name, table_name in file_table_map.items():
        #read files to pandas
        df = pd.read_excel(file_name)

        #format date as per mysql
        for col in date_map.get(file_name,[]):
            df[col]=pd.to_datetime(df[col],format="%d-%m-%Y", errors="coerce")
            data = df
        #Truncate the tables
        conn.execute(text(f"TRUNCATE TABLE {table_name}"))

        df.to_sql(table_name,con=engine,if_exists="append",index=False)

        print(f"{file_name} is updated in the table called {table_name}")

print("All tables successfully importated")

