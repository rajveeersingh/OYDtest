import pandas as pd

inpt_csv = pd.read_csv("/home/superadmin/DBDA/project/OYD/summary.csv")

del inpt_csv['ID']


Limit = int(input("Enter Limit value:- "))

Min_value = float(input("Enter min double value between 0 and 1:- "))

for j in inpt_csv.head(Limit):
    for i in inpt_csv[j].head(Limit):
        if i> Min_value:
            result =pd.DataFrame((f"{j}: ",round(i,9)))
            print(result)
            result.to_csv("/home/superadmin/DBDA/project/OYD/result.csv",mode='a',index=False)