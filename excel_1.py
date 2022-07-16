import pandas as pd
import numpy as np

# Step 1 : Creating the object with pd.ExcelWriter("<filename>")
# Step 2 : df.to_excel(object, sheet_name=, index=,startcol=,startrow=)
# Step 3 : Object.close()

_dict = {
    "Col1" : [1,2,3,4],
    "Col2" : [2,3,4,5],
    "Col3" : [5,6,7,8]
}

df = pd.DataFrame(_dict)

# xl = pd.ExcelWriter("Test.xlsx")
# df.to_excel(xl, sheet_name="Test", index=False)
# xl.close()


# Diff Col in diff sheets
df1 = df[['Col1','Col2']]
print(df1)



xl = pd.ExcelWriter("Test-1.xlsx")
df1.to_excel(xl, sheet_name='FirstSheet', startcol=5, startrow=5, index=False)
xl.close()
