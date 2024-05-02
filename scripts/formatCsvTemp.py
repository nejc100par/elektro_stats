import sys
import pandas as pd
import datetime as dt

df=pd.read_csv(sys.argv[1],delimiter=";")

df['Datum'] = df['Datum'].str.strip()
df['Ura'] = df['Ura'].str.strip()
df['Timestamp'] = pd.to_datetime(df['Datum'] + ' ' + df['Ura'],dayfirst=True)
#print(df.dtypes)

df2 = df[['Timestamp', 'Zunanja temperatura']].copy()
#print(df2.dtypes)
df_filtered = df2[df2['Timestamp'].dt.year == int(sys.argv[2])]

df_filtered.to_csv("../data/temp-"+sys.argv[2]+".csv", index=False)




