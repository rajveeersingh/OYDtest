import pandas as pd




class Testing_csv():
    def __init__(self):
        self.__inpt_csv = pd.read_csv("/home/superadmin/DBDA/project/OYD/summary.csv")
        del self.__inpt_csv['ID']
        self._Limit =0
        self._Min_value=0.0
    def user_input(self):
        self._Limit = int(input("Enter Limit value:- "))
        self._Min_value = float(input("Enter min double value between 0 and 1:- "))
    def csv_writing(self):
        with open("/home/superadmin/DBDA/project/OYD/result.csv", 'a') as f:
            for k in range(len(self.__inpt_csv)):
                for i,j in enumerate(self.__inpt_csv.iloc[k].sort_values(ascending=False).head(self._Limit)):
                    if j>self._Min_value:

                            f.write(f"{self.__inpt_csv.iloc[k].sort_values(ascending=False).head(self._Limit).index[i]}:{round(j,9)},")
                f.write("\n")

obj =Testing_csv()
obj.user_input()
obj.csv_writing()