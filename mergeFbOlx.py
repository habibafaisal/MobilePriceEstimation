import pandas as pd

import pandas as pd
dfOlx = pd.read_csv('olxClean.csv')
dfFb = pd.read_csv('facebookClean.csv')

dfCombined = pd.concat([dfOlx, dfFb], axis=0)

dfCombined.to_csv("FinalCombinedAndCleanedData.csv", index=False)

print(dfCombined.head())
print(dfCombined.tail())