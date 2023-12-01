from yelpapi import YelpAPI
import requests #These 3 packages are for the more complex way to request
import urllib.parse
import json

api_key = 

yelp_api_instance = YelpAPI(api_key)
#2 arguments needed - Search Term & Location Term
search_term = 'pizza'
location_term = 'Chicago, IL'

# # "Non-Fancy way"

search_results = yelp_api_instance.search_query( #"Offset allows you to skip records to access other observations"
    term= search_term, location= location_term,
    sort_by='rating', limit=10
)
#print(search_results)

for business in search_results['businesses']: 
    print('\n')
    print(business)

