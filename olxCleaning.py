import pandas as pd


storedRAM = ["4", "6", "8", "4", "4", "8", "8", "6", "4", "4", "6", "4", "4", "4", "4", "4", "4", "6", "4", "8", "6", "6", "6",
             "4", "4", "4", "2", "8", "4", "6", "4"]
storedROM = ["64", "128", "128", "32", "128", "256", "256", "64", "64", "32", "128", "32", "16", "64", "32", "64", "64",
             "128", "128", "128", "128", "128", "128", "64", "64", "32", "32", "128", "64", "64", "64"]
models = [              "samsung-a-30",
                        "samsung-a-52",
                        "samsung-a-72",
                        "samsung-j-6",
                        "samsung-a-53",
                        "samsung-note-10",
                        "samsung-s-10",
                        "samsung-note-8",
                        "samsung-a-23",
                        "samsung-a-13",
                        "samsung-note-9",
                        "samsung-note-5",
                        "samsung-note-3",
                        "samsung-note-7",
                        "samsung-note-4",
                        "samsung-s-9",
                        "samsung-s-8",
                        "infinix-hot-12",
                        "infinix-note-11",
                        "infinix-zero-8",
                        "infinix-note-10",
                        "infinix-note-7",
                        "infinix-note-8",
                        "infinix-hot-10",
                        "infinix-hot-11",
                        "infinix-hot-9",
                        "infinix-hot-10-play",
                        "infinix-note-12",
                        "infinix-smart-6",
                        "infinix-zero-5",
                        "infinix-s-5",
                        ]

df = pd.read_csv('olx_data.csv')

print(df.head())

condition1 = df['RAM'].astype(float) > 16
df.loc[condition1, 'RAM'] = 0

condition2 = df['RAM'].astype(float) == 10
df.loc[condition2, 'RAM'] = 0

condition3 = df['ROM'].astype(float) > 512
df.loc[condition3, 'ROM'] = 0

import math
condition4 = df['ROM'].astype(float) == 53
df.loc[condition4, 'ROM'] = 0

condition5 = df['ROM'].astype(float) == 265
df.loc[condition5, 'ROM'] = 0

condition6 = df['ROM'].astype(float) == 6
df.loc[condition6, 'ROM'] = 0

condition7 = df['ROM'].astype(float) == 7
df.loc[condition7, 'ROM'] = 0

condition8 = df['ROM'].astype(float) == 11
df.loc[condition8, 'ROM'] = 0

condition9 = df['ROM'].astype(float) == 12
df.loc[condition9, 'ROM'] = 0

condition10 = df['ROM'].astype(float) == 10
df.loc[condition10, 'ROM'] = 0

condition11 = df['ROM'].astype(float) == 96
df.loc[condition11, 'ROM'] = 0

condition11 = df['ROM'].astype(float) == 9
df.loc[condition11, 'ROM'] = 0

df["Location"] = df["Location"].apply(lambda x: x.replace("KhyberPakhtunkhw", "Peshawar"))
df["Location"] = df["Location"].apply(lambda x: x.replace("Punjab", "Lahore"))
df["Location"] = df["Location"].apply(lambda x: x.replace("Sindh", "Karachi"))
df["Location"] = df["Location"].apply(lambda x: x.replace("Balochistan", "Quetta"))


df["Price"] = df["Price"].replace(to_replace ='[A-Za-z]*', value = '', regex = True)

df["Location"] = df["Location"].astype(str).apply(lambda x: x.replace(" ", ""))


#Adding additional columns
df.insert(8, "UpdatedRAM", df["RAM"])

df.insert(9, "UpdatedROM", df["ROM"])

for i in range(len(models)):

    #RAM updated

    condition = ((df['RAM'] == 0) & (df["Model"] == models[i]))
    df.loc[condition, 'UpdatedRAM'] = storedRAM[i]

    print(df.head())

    #ROM updated

    condition = ((df['ROM'] == 0) & (df["Model"] == models[i]))
    df.loc[condition, 'UpdatedROM'] = storedROM[i]

    print(df.head())



df["FinalPrice"]= df["Price"]

df = df.drop(["Description", "RAM", "ROM", "Price"], axis=1)
df.rename(columns={'UpdatedRAM': 'RAM', "UpdatedROM": "ROM", "FinalPrice": "Price"}, inplace=True)

df["Price"] = df["Price"].astype(str).apply(lambda x: x.replace(",", ""))



df.to_csv('olxClean.csv', index=False)

