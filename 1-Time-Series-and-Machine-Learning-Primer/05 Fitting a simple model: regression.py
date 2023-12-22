from sklearn import linear_model

# Prepare input and output DataFrames
X = housing['MedHouseVal'].to_numpy().reshape(-1, 1)
y = housing['AveRooms'].to_numpy().reshape(-1, 1)


# Fit the model
model = linear_model.LinearRegression()
model.fit(X, y)
