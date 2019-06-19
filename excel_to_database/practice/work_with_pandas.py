import pandas as pd

data = pd.ExcelFile('practice.xlsx')
df = pd.read_excel('practice.xlsx', sheetname='Sheet1')

keys = df.keys()
values = df.values
assert 1 == 1