import pandas as pd


df = pd.read_csv('facebook_data.csv', sep='delimiter', on_bad_lines='skip')

df2 = df.iloc[:,0]

df.insert(1, "Brand", "Apple")
df.insert(2, "Model", "Iphone")
df.insert(3, "Condition", "0")
df.insert(4, 'Location', 'Karachi')
df.insert(5, 'RAM', '0')
df.insert(6, 'ROM', '0')
df.insert(7, 'Extract_All', '0')

print(df2.head)
# Model
print('Models')
modelsList=[]
modelsList = df2.str.split(r'(\s?[0-9]+(gb|GB|Gb))', 1)
df['Model'] = modelsList.str[0]
df["ROM"] = modelsList.str[1]
print(df["Model"][12])
df["Model"] = df["Model"].str.strip()
print(df["Model"][12])


# Condition
conditionList = []
conditionList = df2.str.findall(r'[Condition]+\s?:\s?([0-9]+/[0-9]{1,2})').str[0].astype(str).replace({"\[":'', "\]":''}, regex=True)

df['Condition'] = conditionList
print(conditionList)

# main regex
priceList = df2.str.findall(r'\s?[Price\s?|Demand\s?|in\s?|In\s?]\s?:?\s?(\d+|\d{1,3})(,\d+)?(/-)?(?<![\w\d])').astype(str).replace({"\[":'', "\]":'', "\)":'', "\(":''}, regex=True)

df['Price'] = priceList
print(df['Price'])
print(type(df['Price']))

df['Extract_All'] = df.Price.str.findall(r'(\d+(?:\.\d+)?)').astype(str).replace({"\[":'', "\]":''}, regex=True)
print(df['Extract_All'])
print(df["Extract_All"])



df["Condition"] = df["Condition"].apply(lambda x: x.replace("'", ""))
df["Condition"] = df["Condition"].apply(lambda x: x.replace("10/", ""))

# getting the mean and rounding off to 2
avg = df["Condition"].astype(float).mean().round(2)
print("Mean is :", avg)

df["Condition"] = df["Condition"].apply(lambda x: x.replace("nan", str(avg)))

df["Extract_All"] = df["Extract_All"].astype(str).apply(lambda x: x.replace(",", ""))
df["Extract_All"] = df["Extract_All"].astype(str).apply(lambda x: x.replace(" ", ""))
df["Extract_All"] = df["Extract_All"].astype(str).apply(lambda x: x.replace("'", ""))

condition = df['Extract_All'] == ""
df.loc[condition, 'Extract_All'] = 0

condition1 = df['Extract_All'].astype(float) > 500000
df.loc[condition1, 'Extract_All'] = 0

indexZero = df[(df['Extract_All'] == 0)].index
df.drop(indexZero, inplace=True)


df["Model"] = df["Model"].apply(lambda x: x.replace('"', ''))
df["Model"] = df["Model"].apply(lambda x: x.replace(" ", "-"))
df["Model"] = df["Model"].apply(lambda x: x.replace("plus", "+"))
df["Model"] = df["Model"].apply(lambda x: x.replace("--", "-"))
df["Model"] = df["Model"].apply(lambda x: x.replace("Plus", "+"))
df["Model"] = df["Model"].apply(lambda x: x.replace("-x", "-X"))

# df["Model"] = df["Model"].apply(lambda x: x.replace())

df["Model"] = df["Model"].replace(to_replace ='\+.*', value = '+', regex = True)


df["ROM"] = df["ROM"].astype(str).apply(lambda x: x.replace("gb", ""))
df["ROM"] = df["ROM"].astype(str).apply(lambda x: x.replace("Gb", ""))
df["ROM"] = df["ROM"].astype(str).apply(lambda x: x.replace("GB", ""))

df["ROM"] = df["ROM"].astype(str).apply(lambda x: x.replace(" ", ""))

dfFinal = df.drop(['Price', "Posts"], axis=1)
print(dfFinal["Extract_All"])
print(dfFinal.shape)
print(dfFinal.head())


# RAM

# df.insert(8, "UpdatedRAM", df["RAM"])
models = ["Iphone-12-Pro-Max",
          "Iphone-13-Pro-Max",
          "Iphone-13",
          "Iphone-11",
          "Iphone-Xr",
          "Iphone-11-Pro",
          "Iphone-12",
          "Iphone-11-Pro-Max",
          "Iphone-8",
          "Iphone-X",
          "Iphone-7+",
          "Iphone-Xs-Max",
          "Iphone-Xs",
          "Iphone-7",
          "Iphone-8+",
          "Iphone-6s",
          "Iphone-12-Pro",
          "Iphone-13-Pro",

          ]
storedRAM = ["6",
             '6',
             '4',
             "4",
             "3",
             "4",
             "4",
             "4",
             "2",
             "3",
             "3",
             "4",
             "4",
             "2",
             "6",
             "3",
             "2",
             "6"
             ]

for i in range(len(models)):

    #RAM updated

    condition = ((df['RAM'] == '0') & (df["Model"] == models[i]))
    dfFinal.loc[condition, 'RAM'] = storedRAM[i]
    # print(df['UpdatedRAM'])
    # print(df['Model'])
    # print(df['UpdatedRAM'])

# dfFinal["RAM"]= dfFinal["UpdatedRAM"]

# print(dfFinal['UpdatedRAM'])
print(dfFinal['RAM'])
# dfFinal = df.drop(['Price', "Posts", "UpdatedRAM"], axis=1)

# dfFinal.rename(columns = {'Extract_All': 'Price'}, inplace=True)
dfFinal.rename(columns = {'UpdatedRAM': 'RAM','Extract_All': 'Price'}, inplace=True)



dfFinal.to_csv('facebookClean.csv', index=False)

print(dfFinal.iloc[:,0])