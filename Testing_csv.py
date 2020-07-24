import pandas as pd

inpt_csv = pd.read_csv("/home/superadmin/DBDA/project/OYD/summary.csv")

del inpt_csv['ID']

# print(inpt_csv.head(10))

Limit = int(input("Enter Limit value:- "))

Min_value = float(input("Enter min double value between 0 and 1:- "))

for j in inpt_csv.head(Limit):
    for i in inpt_csv[j].head(Limit):
        if i> Min_value:
            print(f"{j}: ",round(i,9))