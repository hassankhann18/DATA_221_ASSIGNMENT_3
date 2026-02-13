import pandas as pd

df = pd.read_csv("crime1.csv")

violent_crime = df["ViolentCrimesPerPop"]

mean_value = violent_crime.mean()
median_value = violent_crime.median()
std_value = violent_crime.std()
min_value = violent_crime.min()
max_value = violent_crime.max()

print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", std_value)
print("Minimum value:", min_value)
print("Maximum value:", max_value)


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
