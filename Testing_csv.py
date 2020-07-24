import pandas as pd



# del inpt_csv['ID']
# print(inpt_csv)

class Testing_csv():
    def __init__(self):
        self.__inpt_csv = pd.read_csv("/home/superadmin/DBDA/project/OYD/summary.csv", index_col='ID')
        self._Limit =0
        self._Min_value=0.0
    def user_input(self):
        self._Limit = int(input("Enter Limit value:- "))

        self._Min_value = float(input("Enter min double value between 0 and 1:- "))
    def csv_writing(self):
        for j in self.__inpt_csv.head(self._Limit):
            for i in self.__inpt_csv[j].head(self._Limit):
                if i> self._Min_value:
                    result =pd.DataFrame(f"{j}: "+str(round(i,9)))
                    result.to_csv("/home/superadmin/DBDA/project/OYD/result.csv",mode='a',index=False)

obj =Testing_csv()
obj.user_input()
obj.csv_writing()