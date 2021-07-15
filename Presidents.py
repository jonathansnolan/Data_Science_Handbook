import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("president_heights.csv")
heights = np.array(data["height(cm)"])

plt.hist(heights)
plt.title('Height Distribution of US Presidents')
plt.xlabel('height (cm)')
plt.ylabel('number')
