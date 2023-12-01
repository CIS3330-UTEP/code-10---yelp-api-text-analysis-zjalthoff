from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

reviews = open('tacos_reviews.txt')
reviews1 = open('ice_cream_reviews.txt')

# for review in reviews:
#     #print(review)
#     sentiment_score = analyzer.polarity_scores(review)
#     print(sentiment_score)

for review in reviews1:
    #print(review)
    sentiment_score = analyzer.polarity_scores(review)
    print(sentiment_score)