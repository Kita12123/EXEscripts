"""
Convert File From .xlsx To .csv

Args:
    .xlsx Filename (str): 変換前ファイル名(.xlsx)
    .csv  Filename (str): 変換後ファイル名(.csv)
"""
import sys
import xlwings as xw
from xlwings.constants import FileFormat

def main(xlsx:str, csv:str):
    wb = xw.Book(xlsx)
    wb.api.SaveAs(csv, Fileformat:=FileFormat.xlCSV)
    wb.close()

if __name__=="__main__":
    FilenameXlsx = sys.argv[1]
    FilenameCsv  = sys.argv[2]
    main(xlsx=FilenameXlsx, csv=FilenameCsv)

    