import numpy as np
import pandas as pd
from pandas import Series, DataFrame

xcl = pd.ExcelFile('Book1.xlsx')

dframe1 = xcl.parse('Sheet1')
print("Sheet1")
print(dframe1)
dframe1.to_csv('1.csv', sep=',');

dframe2 = xcl.parse('Sheet2')
print("Sheet2")
print(dframe2)
dframe2.to_csv('2.csv', sep=',');

dframe3 = xcl.parse('Sheet3')
print("Sheet3")
print(dframe3)
dframe3.to_csv('3.csv', sep=',');

dframe4 = xcl.parse('Sheet4')
print("Sheet4")
print(dframe4)
dframe4.to_csv('4.csv', sep=',');

dframe5 = xcl.parse('Sheet5')
print("Sheet5")
print(dframe5)
dframe5.to_csv('5.csv', sep=',');

dframe6 = xcl.parse('Sheet6')
print("Sheet6")
print(dframe6)
dframe6.to_csv('6.csv', sep=',');

dframe7 = xcl.parse('Sheet7')
print("Sheet7")
print(dframe7)
dframe7.to_csv('7.csv', sep=',');

dframe8 = xcl.parse('Sheet8')
print("Sheet8")
print(dframe8)
dframe8.to_csv('8.csv', sep=',');

dframe9 = xcl.parse('Sheet9')
print("Sheet9")
print(dframe9)
dframe9.to_csv('9.csv', sep=',');

dframe10 = xcl.parse('Sheet10')
print("Sheet10")
print(dframe10)
dframe10.to_csv('10.csv', sep=',');