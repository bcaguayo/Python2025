import pandas as pd

workbook = pd.read_excel("IO\\Barclays.xlsx")

print(next(workbook.iterrows()))

# workbook.head()