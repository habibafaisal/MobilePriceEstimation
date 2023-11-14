import pandas
from sklearn.preprocessing import LabelEncoder

df = pandas.read_csv("FinalCombinedAndCleanedData.csv")

le = LabelEncoder()
df['Brand']= le.fit_transform(df['Brand'])
df['Model']= le.fit_transform(df['Model'])
df['Location']= le.fit_transform(df['Location'])

print(df.head())
print(df.tail(300))

df.to_csv("EncodedFinalCombinedAndCleanedData.csv", index=False)

