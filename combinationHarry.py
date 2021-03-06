# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 11:00:11 2017
@author: cmorris
"""
import pandas as pd
import json
import time
start_time = time.time()
#----------------------------Lexicon setup section-----------------------------

lexicon = pd.read_csv('C:\Users\cmorris\Desktop\Harrys_project\SocialMediaAnalysis\lexicon.csv',header=None, sep=',')

lexicon = lexicon.rename(columns = {0:'word'})
lexicon = lexicon.rename(columns = {1:'anger'})
lexicon = lexicon.rename(columns = {2:'anticipation'})
lexicon = lexicon.rename(columns = {3:'disgust'})
lexicon = lexicon.rename(columns = {4:'fear'})
lexicon = lexicon.rename(columns = {5:'joy'})
lexicon = lexicon.rename(columns = {6:'negative'})
lexicon = lexicon.rename(columns = {7:'positive'})
lexicon = lexicon.rename(columns = {8:'sadness'})
lexicon = lexicon.rename(columns = {9:'suprise'})
lexicon = lexicon.rename(columns = {10:'trust'})
lexicon = lexicon.drop(lexicon.index[0])

lexicon.positive = lexicon.positive.astype(int)
lexicon.negative = lexicon.negative.astype(int)

def get_score(paragraph):
    paragraph=paragraph.lower()
    split_paragraph = paragraph.split()
    score = 0
    for word in split_paragraph:
        
        word_positivity=0
        if word in lexicon.word.values:
            row = lexicon.loc[lexicon.word == word].copy()
            word_positivity=row.positive.values[0]-row.negative.values[0]
        score=score + word_positivity
    return score

#-----------------------------Daily Mail Section-------------------------------

data = []

with open("C:\Users\cmorris\Desktop\Harrys_project\SocialMediaAnalysis\Grenfell_DailyMail_comments.json") as f:
    data = json.loads(f.readline())
    
data=pd.DataFrame(data)

data['id'] = data['from'].apply(lambda x : x['id'])
data['name'] = data['from'].apply(lambda x : x['name'])

#data.loc('id') = data["id"]
#data.loc('name') = data["name"]

data = data.drop('from', 1)
data = data.drop('parent_id', 1)
data = data.drop('id', 1)
data = data.drop('likes', 1)

paragraph=data['message']
data['rating']=data['message'].apply(get_score)

data['ratio'] = data['comment_count']/data['like_count']
Mail_orig = data
data = data[data.like_count != 0]

#--------------------------------BBC Section-----------------------------------

data_BBC = []

with open("C:\Users\cmorris\Desktop\Harrys_project\SocialMediaAnalysis\Grenfell_BBC_comments.json") as g:
    data_BBC = json.loads(g.readline())
    
data_BBC=pd.DataFrame(data_BBC)

data_BBC['id'] = data_BBC['from'].apply(lambda x : x['id'])
data_BBC['name'] = data_BBC['from'].apply(lambda x : x['name'])

#data_BBC.loc('id') = data_BBC["id"]
#data_BBC.loc('name') = data_BBC["name"]

data_BBC = data_BBC.drop('from', 1)
data_BBC = data_BBC.drop('parent_id', 1)
data_BBC = data_BBC.drop('id', 1)
data_BBC = data_BBC.drop('likes', 1)
data_BBC = data_BBC.drop('i', 1)

paragraph=data_BBC['message']
data_BBC['rating']=data_BBC['message'].apply(get_score)

data_BBC['ratio'] = data_BBC['comment_count']/data_BBC['like_count']
BBC_orig = data_BBC
data_BBC = data_BBC[data_BBC.like_count != 0]

#------------------------------Guardian Section--------------------------------

data_guardian = []

with open("C:\Users\cmorris\Desktop\Harrys_project\SocialMediaAnalysis\Grenfell_Guardian_comments.json") as h:
    data_guardian = json.loads(h.readline())
    
data_guardian=pd.DataFrame(data_guardian)

data_guardian['id'] = data_guardian['from'].apply(lambda x : x['id'])
data_guardian['name'] = data_guardian['from'].apply(lambda x : x['name'])

#data_guardian.loc('id') = data_guardian["id"]
#data_guardian.loc('name') = data_guardian["name"]

data_guardian = data_guardian.drop('from', 1)
data_guardian = data_guardian.drop('parent_id', 1)
data_guardian = data_guardian.drop('id', 1)
data_guardian = data_guardian.drop('likes', 1)

paragraph=data_guardian['message']
data_guardian['rating']=data_guardian['message'].apply(get_score)

data_guardian['ratio'] = data_guardian['comment_count']/data_guardian['like_count']
guardian_orig = data_guardian
data_guardian = data_guardian[data_guardian.like_count != 0]

#---------------------------Huffington Post Section----------------------------

data_huff = []

with open("C:\Users\cmorris\Desktop\Harrys_project\SocialMediaAnalysis\Grenfell_HuffingtonPost_comments.json") as h:
    data_huff = json.loads(h.readline())
    
data_huff=pd.DataFrame(data_huff)

data_huff['id'] = data_huff['from'].apply(lambda x : x['id'])
data_huff['name'] = data_huff['from'].apply(lambda x : x['name'])

#data_huff.loc('id') = data_huff["id"]
#data_huff.loc('name') = data_huff["name"]

data_huff = data_huff.drop('from', 1)
data_huff = data_huff.drop('parent_id', 1)
data_huff = data_huff.drop('id', 1)
data_huff = data_huff.drop('likes', 1)

paragraph=data_huff['message']
data_huff['rating']=data_huff['message'].apply(get_score)

data_huff['ratio'] = data_huff['comment_count']/data_huff['like_count']
huff_orig = data_huff
data_huff = data_huff[data_huff.like_count != 0]

#----------------------------Independent Section-------------------------------

data_indy = []

with open("C:\Users\cmorris\Desktop\Harrys_project\SocialMediaAnalysis\Grenfell_Independent_comments.json") as f:
    data_indy = json.loads(f.readline())
    
data_indy=pd.DataFrame(data_indy)

data_indy['id'] = data_indy['from'].apply(lambda x : x['id'])
data_indy['name'] = data_indy['from'].apply(lambda x : x['name'])

#data_indy.loc('id') = data_indy["id"]
#data_indy.loc('name') = data_indy["name"]

data_indy = data_indy.drop('from', 1)
data_indy = data_indy.drop('parent_id', 1)
data_indy = data_indy.drop('id', 1)
data_indy = data_indy.drop('likes', 1)

paragraph=data_indy['message']
data_indy['rating']=data_indy['message'].apply(get_score)

data_indy['ratio'] = data_indy['comment_count']/data_indy['like_count']
indy_orig= data_indy
data_indy = data_indy[data_indy.like_count != 0]

#------------------------------Standard Section--------------------------------

data_standard = []

with open("C:\Users\cmorris\Desktop\Harrys_project\SocialMediaAnalysis\Grenfell_Standard_comments.json") as h:
    data_standard = json.loads(h.readline())
    
data_standard=pd.DataFrame(data_standard)

data_standard['id'] = data_standard['from'].apply(lambda x : x['id'])
data_standard['name'] = data_standard['from'].apply(lambda x : x['name'])

#data_standard.loc('id') = data_standard["id"]
#data_standard.loc('name') = data_standard["name"]

data_standard = data_standard.drop('from', 1)
data_standard = data_standard.drop('parent_id', 1)
data_standard = data_standard.drop('id', 1)
data_standard = data_standard.drop('likes', 1)

paragraph=data_standard['message']
data_standard['rating']=data_standard['message'].apply(get_score)

data_standard['ratio'] = data_standard['comment_count']/data_standard['like_count']
standard_orig = data_standard
data_standard = data_standard[data_standard.like_count != 0]

#---------------------------------Sun Section----------------------------------

data_sun = []

with open("C:\Users\cmorris\Desktop\Harrys_project\SocialMediaAnalysis\Grenfell_TheSun_comments.json") as h:
    data_sun = json.loads(h.readline())
    
data_sun=pd.DataFrame(data_sun)

data_sun['id'] = data_sun['from'].apply(lambda x : x['id'])
data_sun['name'] = data_sun['from'].apply(lambda x : x['name'])

#data_sun.loc('id') = data_sun["id"]
#data_sun.loc('name') = data_sun["name"]

data_sun = data_sun.drop('from', 1)
data_sun = data_sun.drop('parent_id', 1)
data_sun = data_sun.drop('id', 1)
data_sun = data_sun.drop('likes', 1)

paragraph=data_sun['message']
data_sun['rating']=data_sun['message'].apply(get_score)

data_sun['ratio'] = data_sun['comment_count']/data_sun['like_count']
sun_orig = data_sun
data_sun = data_sun[data_sun.like_count != 0]

#-----------------------------Telegraph Section--------------------------------

data_tely = []

with open("C:\Users\cmorris\Desktop\Harrys_project\SocialMediaAnalysis\Grenfell_Telegraph_comments.json") as h:
    data_tely = json.loads(h.readline())
    
data_tely=pd.DataFrame(data_tely)

data_tely['id'] = data_tely['from'].apply(lambda x : x['id'])
data_tely['name'] = data_tely['from'].apply(lambda x : x['name'])

#data_tely.loc('id') = data_tely["id"]
#data_tely.loc('name') = data_tely["name"]

data_tely = data_tely.drop('from', 1)
data_tely = data_tely.drop('parent_id', 1)
data_tely = data_tely.drop('id', 1)
data_tely = data_tely.drop('likes', 1)

paragraph=data_tely['message']
data_tely['rating']=data_tely['message'].apply(get_score)

data_tely['ratio'] = data_tely['comment_count']/data_tely['like_count']
tely_orig = data_tely
data_tely = data_tely[data_tely.like_count != 0]

#----------------------------Combination Section-------------------------------

combined=data_tely.append([data_sun, data_standard, data_indy, data_huff, data_guardian, data_BBC, data])

combined_with_0s=tely_orig.append([sun_orig, standard_orig, indy_orig, huff_orig, guardian_orig, BBC_orig, Mail_orig])

#----------------------------Evaluation Section--------------------------------

#The Daily Mail positive - negative ratio = 1.14583333333
#The Daily Mail mean = 0.0154639175258 (article was 3)
#The BBC positive - negative ratio = 1.27319587629
#The BBC mean = 0.0623376623377 (article was 0)
#The Guardian positive - negative ratio = 1.09550561798
#The Guardian mean = 0.150362318841 (article was 0)
#The Huffington Post positive - negative ratio = 1.06504065041
#The Huffington Post mean = 0.154761904762 (article was 0)
#The Independent positive - negative ratio = 1.73384030418
#The Independent mean = 0.286971830986 (article was 1)
#The Standard positive - negative ratio = 5.66
#The Standard mean = 0.748633879781 (article was 0)
#The Sun positive - negative ratio = 1.24324324324
#The Sun mean = 0.207547169811 (article was -1)
#The Telegraph positive - negative ratio = 1.75
#The Telegraph mean = 0.738372093023 (article was 2)

print(data['rating'].describe())
print(data_BBC['rating'].describe())
print(data_guardian['rating'].describe())
print(data_huff['rating'].describe())
print(data_indy['rating'].describe())
print(data_standard['rating'].describe())
print(data_sun['rating'].describe())
print(data_tely['rating'].describe())

print("My program took", time.time() - start_time, "to run")

s = pd.Series(data =[ 0.2, 0.3, 0.5], index = ['a','b','c'])