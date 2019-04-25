import matplotlib
matplotlib.use('Agg')
import pandas as pd
import seaborn as sns
import numpy as np

def power(sample1, sample2, reps, size, alpha = 0.05):
□ 1: Repeat reps times:
□ 1.a: generate a new sample from the first sample
□ 1.b: Generate a new sample form the second sample
□ 1.c: Compare the two samples and calculate the p-value
□ 2: Return the percentage of times that the p-value was < 1-alpha


if __name__ == "__main__":
	df = pd.read_csv('./salaries.csv')

	data = df.values.T[1]
