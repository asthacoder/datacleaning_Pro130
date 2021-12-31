import pandas as pd
import csv
df = pd.read_csv("pro130.csv")
print(df.shape)

df.drop(['Unnamed: 0','Unnamed: 6', 'Star_name.1', 'Distance.1', 
'Mass.1', 'Radius.1','Luminosity'],axis=1,inplace=True)

final_data = df.dropna()
final_data.to_csv('final_data.csv')