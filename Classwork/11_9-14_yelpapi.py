from yelpapi import YelpAPI
import requests #These 3 packages are for the more complex way to request
import urllib.parse
import json
import pandas as pd


api_key = ""

yelp_api_instance = YelpAPI(api_key)
#2 arguments needed - Search Term & Location Term
search_term = 'pizza'
location_term = 'Chicago, IL'



# # "Non-Fancy way" BUSN SEARCH QUERY (NON-PANDAS)


search_results = yelp_api_instance.search_query( #"Offset allows you to skip records to access other observations"
    term= search_term, location= location_term,
    sort_by='rating', limit=10#, offset=10
)
# print(search_results)

# # BUSN SEARCH W/ PANDAS

# result_df = pd.DataFrame.from_dict(search_results['businesses']) #Useful for storing queried data (avoid API costs) 'dfname.to_csv(csvname, index=FALSE)'
# print(result_df)

# for business in search_results['businesses']: 
#     print('\n')
#     print(business)


# # REVIEW SEARCH QUERY

# # # W/ PANDAS
id_for_reviews = 'bob-s-pizza-chicago'

review_response = yelp_api_instance.reviews_query(id=id_for_reviews)

reviews_df = pd.DataFrame.from_dict(review_response['reviews'])
reviews_df.to_csv #SEE SLIDES FOR FINISH


# # # NON-PANDAS
# for review in review_response['reviews']: #Max output of 3 views 
#     print("\n")
#     print(review)
