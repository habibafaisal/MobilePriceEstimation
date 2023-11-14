import pandas
from sklearn.preprocessing import LabelEncoder
from sklearn import linear_model
from sklearn.model_selection import train_test_split
df = pandas.read_csv("EncodedFinalCombinedAndCleanedData.csv")


X = df[["Brand", "Model", "Condition", "Location", 'RAM', "ROM"]]
Y = df['Price']

# X = pandas.get_dummies(data=X, drop_first=True)

print(X)


X_train, X_test, Y_train, Y_test = train_test_split(X,Y , test_size=0.2, random_state=40)
regr = linear_model.LinearRegression()
regr.fit(X_train, Y_train)
predicted = regr.predict(X_test)

print(predicted)
# print(regr.predict([[0, 5, 45, 6, 256]]))
# print(regr.predict([[1, 12, 9, 50, 8, 128]]))
# print(regr.predict([[2, 12, 9, 50, 8, 256]]))
