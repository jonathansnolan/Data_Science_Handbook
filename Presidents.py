import pandas as pd
import numpy as np
x = pd.read_csv("president_heights.csv")
heights = np.array(x["height(cm)"])


# print(x.head())
# print(height)

print("Mean height:       ", heights.mean())
print("Standard deviation:", heights.std())
print("Minimum height:    ", heights.min())
print("Maximum height:    ", heights.max())
