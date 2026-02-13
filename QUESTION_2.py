import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("crime1.csv")

violent_crime = df["ViolentCrimesPerPop"]

# HISTOGRAM
plt.figure()
plt.hist(violent_crime, bins=20)
plt.title("Violent Crimes Per Population")
plt.xlabel("ViolentCrimesPerPop")
plt.ylabel("Frequency")
plt.show()

# Box Plot
plt.figure()
plt.boxplot(violent_crime)
plt.title("Violent Crimes Per Population")
plt.xlabel("ViolentCrimesPerPop")
plt.ylabel("Values")
plt.show()

# COMMENTS / INTERPRETATION

# Histogram shows that most values of ViolentCrimesPerPop
# are concentrated at the lower end of the scale, with fewer communities having very high crime rates.
# This indicates that the data is not evenly spread and is skewed.
# The box plot shows the median as the line inside the box,
# which is closer to the lower values, confirming the skewness.
# The presence of points beyond the whiskers tells
# that there are outliers in the data which represents unusually high violent crime rates.

