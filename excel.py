from openpyxl import Workbook, load_workbook
#when creating a file to store it should be xlxs for excel files anyway
import pandas as pd
#You can read an Excel file into a pandas DataFrame using the read_excel function from the pandas library

func = pd.read_excel("dummydata2.xlsx")
#print(func)
#descriptive part
descrption = func.describe()
print(descrption)
