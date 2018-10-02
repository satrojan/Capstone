import glob
import pandas as pd

# get data file names
path =r'/data'
filenames = glob.glob("./data/science/*")
filenames
dfs = []
for filename in filenames:
    dfs.append(pd.read_csv(filename))

# Concatenate all data into one DataFrame
big_frame = pd.concat(dfs, ignore_index=True)

big_frame.drop('Unnamed: 0', axis=1, inplace=True)

big_frame.to_csv('./data/science_final.csv')
