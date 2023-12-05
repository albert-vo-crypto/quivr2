from langchain.document_loaders import CSVLoader
from models.files import File

from .common import process_file

# importe required libraries
import openpyxl
import requests
import pandas as pd
import os
import sys
from langchain.document_loaders import UnstructuredExcelLoader
import shutil

'''
# open given workbook 
# and store in excel object 
excel = openpyxl.load_workbook("Test.xlsx")
  
# select the active sheet
sheet = excel.active
  
# writer object is created
col = csv.writer(open("tt.csv",
                      'w', 
                      newline=""))
  
# writing the data in csv file
for r in sheet.rows:
    # row by row write 
    # operation is perform
    col.writerow([cell.value for cell in r])
  
# read the csv file and 
# convert into dataframe object 
df = pd.DataFrame(pd.read_csv("tt.csv"))
  
# show the dataframe
df

'''
'''
excel_file = 'context_data/data/excel_file.xlsx'
all_sheets = pd.read_excel(excel_file, sheet_name=None)
sheets = all_sheets.keys()

for sheet_name in sheets:
    sheet = pd.read_excel(excel_file, sheet_name=sheet_name)
    sheet.to_csv("context_data/data/%s.csv" % sheet_name, index=False)
'''
def process_xlsx(
    file: File,
    enable_summarization,
    brain_id,
    user_openai_api_key,
):
    
    '''
    excel_file = 'context_data/data/excel_file.xlsx'
    all_sheets = pd.read_excel(excel_file, sheet_name=None)
    sheets = all_sheets.keys()

    for sheet_name in sheets:
        sheet = pd.read_excel(excel_file, sheet_name=sheet_name)
        sheet.to_csv("context_data/data/%s.csv" % sheet_name, index=False)

    '''
    print ("Hello! BEFORE XLSX to CSV inside process_xlsx", os.path.abspath(file.file_name), os.getcwd(), file.file_name)
    
    excel_file = file.file_name
    excel_file2 = "/home/avo/SWIFT-ESG/QUIVER3/quivr/backend/" + excel_file.strip()
    file_csv_out : File
    file_csv_out = file
    print ("excel_file2 = ", excel_file2)
    print ("excel_file2_out = ", file_csv_out)
    #all_sheets = pd.read_excel(excel_file2, sheet_name=None)


    
    print ("Hello! AFTER XLSX to CSV inside process_xlsx", os.path.abspath(__file__), os.getcwd(), file.file_name)

    return process_file(
        file=file,
        loader_class=UnstructuredExcelLoader,
        enable_summarization=enable_summarization,
        brain_id=brain_id,
        user_openai_api_key=user_openai_api_key,
    )
