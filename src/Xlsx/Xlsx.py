from tkinter import *
from tkinter import filedialog
import os
import openpyxl
def SearchFilePath_Xlsx():
    """
    选择xlsx文件
    :return: 返回选择的xlsx文件地址
    """
    root = Tk()
    root.withdraw()
    FilePath = filedialog.askopenfilename(title='Select The xlsx file', filetypes=[('xlsx files', '*.xlsx')],
    initialdir=os.getcwd())
    file_path, file_name = os.path.split(FilePath)
    os.chdir(file_path)
    return FilePath
def read_Xlsx(ExcelPath,SheetName = 'Sheet1'):
    """
    读取xlsx文件
    :param ExcelPath: xlsx文件地址
    :return: xlsx对象，sheet 对象
    """
    workbook = openpyxl.load_workbook(ExcelPath)
    # 选择工作表
    sheet = workbook[SheetName]
    return workbook, sheet