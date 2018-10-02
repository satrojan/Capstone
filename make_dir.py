#!/usr/bin/python

import os, sys
import pandas as pd
# Path to be created

df=pd.read_csv('./workfile.csv')

for i in df.sub_name.values:
	path = "data/{}".format(i)
	os.mkdir(path);

#print "Path is created"
