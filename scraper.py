import numpy as np
import pandas as pd
import datetime
import praw

subreddit_title = pd.read_csv('./workfile.csv')

reddit = praw.Reddit(client_id='lTmx7ljJA-06sw',
                     client_secret='DqoKcVA4JfGW1kPH2hDXO3o7zZM',
                     user_agent='GA_test_Bot',
                     username='GA_test5467943',
                     password='kSYRwtPOY4W0mTderAT4')

def Reddit_Scraper(sub_reddit, catagory, posts):
    title =[]
    comments_author_lst = []
    comments_score_lst = []
    author=[]
    guilded=[]
    num_comments=[]
    score=[]
    pinned = []
    subreddit=[]
    created_utc=[]
    r_id = []

    if catagory == 0:
        cat ='hot'
        #count = 0
        for submission in reddit.subreddit(sub_reddit).hot(limit=posts):
            #print(count)
            #try:
            #count+=1
            title.append(submission.title)
            auth=[]
            sco = []
            sub = reddit.submission(id=submission.id)
            for top_level_comment in sub.comments:
                #print(top_level_comment.score)
                try:
                    auth.append(top_level_comment.author)
                except:
                    auth.append('')
                try:
                    sco.append(top_level_comment.score)
                except:
                    sco.append(0)
            auth = list(map(str,auth))
            if len(auth)>10:
                auth = auth[0:9]
            sco = list(map(int,sco))
            if len(sco)>10:
                sco = sco[0:9]
            #print(sco)
            #print(auth)
            if auth:#check for empty list
                df_temp = pd.DataFrame({'author_comments':auth,'score_comments':sco})
                #print(df_temp.author_comments[0])
                #print(df_temp.score_comments[0])
                df_temp = df_temp[df_temp.author_comments!='None']
                df_temp = df_temp[df_temp.score_comments>df_temp.score_comments.mean()]
                df_temp.sort_values('score_comments',ascending=False,inplace=True)
                comments_author_lst.append(list(df_temp.author_comments))
                comments_score_lst.append(list(df_temp.score_comments))
                del df_temp
            else:
                comments_author_lst.append(np.NaN)
                comments_score_lst.append(np.NaN)
            author.append(submission.author)
            guilded.append(submission.gilded)
            num_comments.append(submission.num_comments)
            score.append(submission.score)
            pinned.append(submission.pinned)
            subreddit.append(submission.subreddit)
            #author_flair_text.append(submission.author_flair_text)
            created_utc.append(submission.created_utc)
            r_id.append(submission.id)
            #body.append(submission.selftext)

    elif catagory == 1:
        cat='new'
        for submission in reddit.subreddit(sub_reddit).new(limit=posts):
            title.append(submission.title)
            comments.append(submission.comments)
            author.append(submission.author)
            guilded.append(submission.gilded)
            num_comments.append(submission.num_comments)
            score.append(submission.score)
            pinned.append(submission.pinned)
            subreddit.append(submission.subreddit)
            #author_flair_text.append(submission.author_flair_text)
            created_utc.append(submission.created_utc)
            r_id.append(submission.id)
            #body.append(submission.selftext)

    elif catagory==2:
        cat='rising'
        for submission in reddit.subreddit(sub_reddit).rising(limit=posts):
            title.append(submission.title)
            comments.append(submission.comments)
            author.append(submission.author)
            guilded.append(submission.gilded)
            num_comments.append(submission.num_comments)
            score.append(submission.score)
            pinned.append(submission.pinned)
            subreddit.append(submission.subreddit)
            #author_flair_text.append(submission.author_flair_text)
            created_utc.append(submission.created_utc)
            r_id.append(submission.id)
            #body.append(submission.selftext)


    elif catagory == 3:
        cat='controvertial'
        for submission in reddit.subreddit(sub_reddit).controversial(limit=posts):
            title.append(submission.title)
            comments.append(submission.comments)
            author.append(submission.author)
            guilded.append(submission.gilded)
            num_comments.append(submission.num_comments)
            score.append(submission.score)
            pinned.append(submission.pinned)
            subreddit.append(submission.subreddit)
            #author_flair_text.append(submission.author_flair_text)
            created_utc.append(submission.created_utc)
            r_id.append(submission.id)
    #print(len(title))
    #print(len(comments_author_lst))
    #print(len(comments_score_lst))
    #print(len(author))
    #print(len(guilded))
    #print(len(num_comments))
    #print(len(pinned))
    #print(len(subreddit))
    #print(len(created_utc))
    #print(len(r_id))
    #print(len(score))
    df_temp = pd.DataFrame({'title': title,
                        'comments_author_lst': comments_author_lst,
                        'comments_score_lst': comments_score_lst,
                        'author' :author,
                        'guilded':guilded,
                        'num_comments':num_comments,
                        'score':score,
                        'pinned':pinned,
                        'subreddit':subreddit,
                        #'author_flair_text':author_flair_text,
                        'created_utc':created_utc,
                        'r_id':r_id})
                        #'body':body})


    tme = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    f_name='./data/{}/{}_{}_{}.csv'.format(sub_reddit,tme,cat,sub_reddit)
    df_temp.to_csv(f_name)
    del df_temp

for i in subreddit_title.sub_name:
	print(i)
	Reddit_Scraper(i,0,400)

#Reddit_Scraper('AskReddit',0,400)
#Reddit_Scraper('politics',0,400)
#Reddit_Scraper('The_Donald',0,400)
#Reddit_Scraper('worldnews',0,400)
#Reddit_Scraper('nba',0,400)

#askreddit

#Reddit_Scraper('Showerthoughts',0,400)
##Reddit_Scraper('NoStupidQuestions',0,400)
#Reddit_Scraper('AskOuija',0,400)
#Reddit_Scraper('Jokes',0,400)
#Reddit_Scraper('explainlikeimfive',0,400) #         77

#the _donald

#Reddit_Scraper('news',0,400) #               17
#Reddit_Scraper('yankees',0,400) #                 15
#Reddit_Scraper('opieandanthony',0,400) #           8
#Reddit_Scraper('PoliticalHumor',0,400) #           7
#Reddit_Scraper('funny',0,400) #                    6

#nba

#Reddit_Scraper('soccer',0,400) #                  21
#Reddit_Scraper('NBA2k',0,400) #                   18
#Reddit_Scraper('lakers',0,400) #                  14
#Reddit_Scraper('nfl',0,400) #                     12
#Reddit_Scraper('timberwolves',0,400) #            11
#Reddit_Scraper('hiphopheads',0,400) #             11

#politics

#Reddit_Scraper('nottheonion',0,400) #             26
#Reddit_Scraper('technology',0,400) #              16
#Reddit_Scraper('GameLive_0n',0,400) #             15
#Reddit_Scraper('videos',0,400) #                  12
#Reddit_Scraper('TwoXChromosomes',0,400) #         11

#worldnews

#Reddit_Scraper('india',0,400) #                    38
#Reddit_Scraper('todayilearned',0,400) #            12
#Reddit_Scraper('europe',0,400) #                    9
#Reddit_Scraper('Futurology',0,400) #                8
#Reddit_Scraper('science',0,400) #                   7
