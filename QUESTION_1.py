import pandas as pd

df = pd.read_csv("crime1.csv")

violent_crime = df["ViolentCrimesPerPop"]

mean_value = violent_crime.mean()
median_value = violent_crime.median()
standard_diviation_value = violent_crime.std()
minimum_value = violent_crime.min()
maximum_value = violent_crime.max()

print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", standard_diviation_value)
print("Minimum value:", minimum_value)
print("Maximum value:", maximum_value)


# QUESTION 1
# Comparison of mean and median:
# The mean is greater than the median.
# This means that the distribution of ViolentCrimesPerPop is right-skewed (positively skewed).
# This means there are some communities with very high crime values that pull the mean upward.

# QUESTION 2
# Effect of extreme values:
# The mean is more affected by extreme values than the median.
# This is because the mean uses all data values in its calculation,
# while the median depends only on the middle value.
