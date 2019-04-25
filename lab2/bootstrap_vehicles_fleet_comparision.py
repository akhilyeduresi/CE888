import matplotlib
matplotlib.use('Agg')
import pandas as pd
import seaborn as sns
import numpy as np


def boostrap(sample, sample_size, iterations):
	sample_data = np.random.choice(sample, size=(iterations, sample_size))

	data_mean = np.mean(sample_data)
	lower = np.percentile(sample_data,2.5)
	upper = np.percentile(sample_data, 97.5)
	# <---INSERT YOUR CODE HERE--->
	return data_mean, lower, upper


def get_bootstrap(data):
	boots = []
	for i in range(100, 100000, 1000):
		boot = boostrap(data, data.shape[0], i)
		boots.append([i, boot[0], "mean"])
		boots.append([i, boot[1], "lower"])
		boots.append([i, boot[2], "upper"])
	return boots


if __name__ == "__main__":
	df = pd.read_csv('./vehicles.csv')

	data = df.values.T[0]
	boots = get_bootstrap(data)

	df_boot = pd.DataFrame(boots, columns=['Boostrap Iterations', 'Mean', "Value"])
	sns_plot = sns.lmplot(df_boot.columns[0], df_boot.columns[1], data=df_boot, fit_reg=False, hue="Value")

	sns_plot.axes[0, 0].set_ylim(0,)
	sns_plot.axes[0, 0].set_xlim(0, 100000)

	sns_plot.savefig("bootstrap_confidence_current_fleet.png", bbox_inches='tight')
	sns_plot.savefig("bootstrap_confidence_current_fleet.pdf", bbox_inches='tight')

	boots = get_bootstrap(df.values[1])
	df_boot = pd.DataFrame(boots, columns=['Boostrap Iterations', 'Mean', "Value"])
	sns_plot = sns.lmplot(df_boot.columns[0], df_boot.columns[1], data=df_boot, fit_reg=False, hue="Value")

	sns_plot.axes[0, 0].set_ylim(0,)
	sns_plot.axes[0, 0].set_xlim(0, 100000)

	sns_plot.savefig("bootstrap_confidence_new.png", bbox_inches='tight')
	sns_plot.savefig("bootstrap_confidence_new.pdf", bbox_inches='tight')


	#print("Mean: %f"%(np.mean(data )))
	#print("Var: %f"%(np.var(data)))
	


	