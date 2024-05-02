import sys
import pandas as pd

 #First column of data usuallz doesn't have delimiter at the end
data=pd.read_csv(sys.argv[1],delimiter=";",decimal=",",parse_dates=["Datum"])
data.drop('Merilno mesto', inplace=True, axis=1) 
data.drop('GSRN MM', inplace=True, axis=1)
data.to_csv("../data/elektro-"+sys.argv[2]+".csv", index=False)




