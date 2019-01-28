import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv("M://CE888//CE888//Lab2//vehicles.csv")
print(data.head())
data.rename(columns={"Current fleet": "C", "New Fleet": "N"},inplace='True')
print(data.head())
import numpy as np
sns.distplot(data["C"]).get_figure()
plt.show()