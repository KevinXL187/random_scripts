import pandas as pd
import statsmodels.api as sm

data = {
    'Y': [47, 38, 47, 39, 44, 64, 58, 49, 55, 52, 49, 47, 40, 42, 63, 40, 59, 56, 76, 67, 57, 57, 42, 54, 60, 33, 55, 36, 36, 42, 41, 42, 39, 27, 31, 39, 56, 40, 58, 43, 40, 46, 50],
    'X1': [287, 236, 255, 135, 121, 171, 260, 237, 261, 397, 259, 261, 258, 280, 339, 161, 324, 171, 265, 280, 248, 192, 349, 263, 223, 316, 288, 256, 318, 270, 262, 264, 325, 388, 260, 284, 326, 248, 285, 361, 248, 289, 270],
    'X2': [111, 135, 98, 63, 46, 103, 227, 157, 266, 167, 164, 119, 145, 247, 168, 68, 92, 56, 240, 306, 93, 115, 408, 103, 102, 274, 130, 149, 180, 134, 154, 86, 148, 191, 123, 135, 236, 92, 153, 126, 226, 176, 180]
}

# Create DataFrame
df = pd.DataFrame(data)
X = sm.add_constant(df[['X1', 'X2']])
Y = df['Y']
model = sm.OLS(Y, X).fit()

print(model.summary())
new_data = pd.DataFrame({'const': [1], 'X1': [300], 'X2': [150]})
prediction = model.get_prediction(new_data)

# Confidence interval for mean response
print(prediction.conf_int(alpha=0.05))

# Prediction interval for new observation
print(prediction.conf_int(obs=True, alpha=0.05))