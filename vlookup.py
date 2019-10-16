import pandas as pd

class Data_Lookup():
  def __init__(self):
    pass
  def getData(self):
    sheetdata = input("Enter 1 if data is in 2 excel files, 0 if data is in same excel file with in 2 sheets : ")
    # sheetdata = 0
    if int(sheetdata) == 1:
      filename1 = str(input("Enter File1 Name : ") + ".xlsx")
      print(filename1)
      filename2 = input("Enter File2 Name : ")
      file1 = pd.read_excel(filename1,header=None)
      file2 = pd.read_excel(filename2,header=None)
      sheet1_name = None
      sheet2_name = None
    elif int(sheetdata) == 0:
      sheet1_name = input("Enter sheet name of data with only ID's :")
      sheet2_name = input("Enter sheet name with entire data :")
      # sheet1_name = "Sheet1"
      # sheet2_name = "Sheet2"
      file1 = pd.read_excel('file2.xlsx',sheet_name= sheet2_name, header=None)
      file2 = pd.read_excel('file2.xlsx',sheet_name= sheet1_name, header=None)
    else:
      print("Please enter valid data")
      self.getData()
    return file1, file2

  def getColumnData(self):
    file1_col = int(input("Enter Column number from file1 to compare :"))
    # file1_col = 0
    file2_col = int(input("Enter Column number from file2 to compare with file1:"))
    file2_col2 = int(input("Enter column number to copy data to file1 :"))
    # file2_col = 0
    # file2_col2 = 4
    return file1_col, file2_col, file2_col2
    
  def dataManipulation(self, file1, file2, file1_col, file2_col, file2_col2):
    file3_list =  []
    for i in range(len(file1)):
      flag = 0
      for j in range(len(file2)):
        if str(file1[file1_col][i]) == str(file2[file2_col][j]):
          flag = 1
          break
      if flag == 1:
        file3_list.append(file2[file2_col2][j])
      else:
        file3_list.append(None)
    file3 = file1
    file3[1] = file3_list
    print(file3)
    return file3
    
  def excel_Writer(self, file3):
    print("reached here")
    file3.to_csv("file3.csv",index=False, header=False)
    print("done")

  def __main__(self):
    file1, file2 = self.getData()
    file1_col, file2_col, file2_col2 = self.getColumnData()
    file3 = self.dataManipulation(file1, file2, file1_col, file2_col, file2_col2)
    self.excel_Writer(file3)

obj = Data_Lookup()
obj.__main__()