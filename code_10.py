import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import FreqDist
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from yelpapi import YelpAPI
import pandas as pd
import requests #These 3 packages are for the more complex way to request
import urllib.parse
import json
import random
import matplotlib.pyplot as plt

api_key = ""

yelp_api_instance = YelpAPI(api_key)


# # # Business Search & CSV


search_term = 'barbecue'
location_term = 'Austin, TX'

search_results = yelp_api_instance.search_query(term=search_term, location=location_term, sort_by='review_count', limit=40)
bbq_busn_df = pd.DataFrame.from_dict(search_results['businesses'])
print(bbq_busn_df)
bbq_busn_df.to_csv('Austin_bbq_businesses.csv')

busn_df = pd.read_csv('Austin_bbq_businesses.csv')
analyze_list = []
for i in range(10):
    business = random.choice(busn_df['alias'])
    analyze_list.append(business)
print(analyze_list)


# # # Reviews Search & CSV


id1_for_reviews = 'moonshine-patio-bar-and-grill-austin'
id2_for_reviews = 'franklin-barbecue-austin'
id3_for_reviews = 'stiles-switch-bbq-and-brew-austin'
id4_for_reviews = 'coopers-old-time-pit-bar-b-que-austin'
id5_for_reviews = 'brothertons-black-iron-barbecue-pflugerville-7'
id6_for_reviews = 'terry-blacks-barbecue-austin'
id7_for_reviews = 'its-all-good-bbq-spicewood-5'
id8_for_reviews = 'stubbs-bar-b-q-austin'
id9_for_reviews = 'opies-bbq-spicewood'
id10_for_reviews = 'donns-bbq-austin-2'


review_response1 = yelp_api_instance.reviews_query(id=id1_for_reviews)
review_response2 = yelp_api_instance.reviews_query(id=id2_for_reviews)
review_response3 = yelp_api_instance.reviews_query(id=id3_for_reviews)
review_response4 = yelp_api_instance.reviews_query(id=id4_for_reviews)
review_response5 = yelp_api_instance.reviews_query(id=id5_for_reviews)
review_response6 = yelp_api_instance.reviews_query(id=id6_for_reviews)
review_response7 = yelp_api_instance.reviews_query(id=id7_for_reviews)
review_response8 = yelp_api_instance.reviews_query(id=id8_for_reviews)
review_response9 = yelp_api_instance.reviews_query(id=id9_for_reviews)
review_response10 = yelp_api_instance.reviews_query(id=id10_for_reviews)

reviews_df1 = pd.DataFrame.from_dict(review_response1['reviews'])
reviews_df2 = pd.DataFrame.from_dict(review_response2['reviews'])
reviews_df3 = pd.DataFrame.from_dict(review_response3['reviews'])
reviews_df4 = pd.DataFrame.from_dict(review_response4['reviews'])
reviews_df5 = pd.DataFrame.from_dict(review_response5['reviews'])
reviews_df6 = pd.DataFrame.from_dict(review_response6['reviews'])
reviews_df7 = pd.DataFrame.from_dict(review_response7['reviews'])
reviews_df8 = pd.DataFrame.from_dict(review_response8['reviews'])
reviews_df9 = pd.DataFrame.from_dict(review_response9['reviews'])
reviews_df10 = pd.DataFrame.from_dict(review_response10['reviews'])

culm_df = pd.concat([reviews_df1,reviews_df2,reviews_df3,reviews_df4,reviews_df5,reviews_df6,reviews_df7,reviews_df8,reviews_df9,reviews_df10]).sort_index()
culm_df['text'].to_csv('A_bbq_review_text.csv',index=False)


# # # Analysis of Reviews


# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)

reviews = pd.read_csv('A_bbq_review_text.csv')
reviews_df = reviews['text']
stop_words = set(stopwords.words('english'))

# # SENTIMENT ANALYSIS

analyzer = SentimentIntensityAnalyzer()
for review in reviews_df:
    sentiment = analyzer.polarity_scores(review)
    # print(sentiment)
    # print(review)
    # print("\n")

# # REMOVE STOP WORDS

new_rev = []
for review in reviews_df:
    words = nltk.word_tokenize(review.lower())
    #print(words)
    for word in words:
        if word not in stop_words and word.isalnum():
            new_rev.append(word)

#print(new_rev)

# # WORD FREQUENCY

frequency = FreqDist(new_rev)
most_common_words = frequency.most_common(20)
print(f"Most Common Words in the Review Data:{most_common_words}")

# frequency.plot(20, cumulative=False)
# plt.show()

# # # OPENAI HELP (Unused in the end)

# def remove_stopwords(text): # Help from OpenAI in creating this function. Modified and added to it for the project
#     stop_words = set(stopwords.words('english'))
#     words = nltk.word_tokenize(text)
#     filtered_words = [word for word in words if word.lower() not in stop_words]
#     return ' '.join(filtered_words)

# for review in reviews_df:
#     filtered_review = remove_stopwords(review)
#     new_rev.append(filtered_review)