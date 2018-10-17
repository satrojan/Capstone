import glob
import pandas as pd

df=pd.read_csv('./workfile.csv')

for i in df.sub_name.values:
	print(i)

	# get data file names
	path =r'/data'
	filenames = glob.glob("./data/{}/*".format(i))
	filenames
	dfs = []

	for filename in filenames:
    		dfs.append(pd.read_csv(filename))

	# Concatenate all data into one DataFrame
	big_frame = pd.concat(dfs, ignore_index=True)

	big_frame.drop('Unnamed: 0', axis=1, inplace=True)

	big_frame.to_csv('./data/{}_final.csv'.format(i))
