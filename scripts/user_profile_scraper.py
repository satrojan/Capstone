import numpy as np
import pandas as pd
import requests
import json


df = pd.read_csv('./workfile.csv')
for z in df.sub_name.values:


	df_sub = pd.read_csv('./data/{}_final.csv'.format(z))

	df_sub.drop_duplicates('author',inplace=True)

	auth_lst=df_sub.author.values
	#print(auth_lst)
	sub_lst = []
	for i in auth_lst:
		#print(i)
		try:
			json_link  = 'https://www.reddit.com/user/{}/.json'.format(i)
			res = requests.get(json_link, headers={'User-agent': 'Capstone Bot 0.1'})
			data = res.json()
		
			df=pd.DataFrame(data)
			#print('first')
			try:
				#print('second')
				df=pd.DataFrame(df.T.children[1])
			except:
            			continue
			for i in range(24):
				if len(df.data[i])==94:
					#print(df.data[i]['subreddit'])
					sub_lst.append(df.data[i]['subreddit'])
        	#print(sub_lst[-1])
		except:
			continue

		df = pd.DataFrame({'subreddits':sub_lst})


	df.to_csv('./data/{}_posters_lst.csv'.format(z),index=False)

