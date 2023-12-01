import nltk
from nltk.corpus import stopwords

reviews = open('ice_cream_reviews.txt')
stop_words = set(stopwords.words('english')) #set makes list immutable (recommended)

# # Alternative ways to read the reviews
# print(reviews.read())

for review in reviews: 
    print("\n")
    print(review)
    tokens = nltk.word_tokenize(review)     #TOKENIZATION
    # print(tokens)
    pos_tags = nltk.pos_tag(tokens)     #PARTS OF SPEECH - look at POS dictionary
    # print(pos_tags)
    new_text = []
    for tag in pos_tags: #FIND SPECIFIC POS
        # if tag[1] == 'JJ' or tag[1] == 'JJR' or tag[1] == 'JJS': #tag 1 (2nd tag) is the pos tag
            # print(tag)
        # if tag[1] == 'NN' or tag[1] == 'NNP' or tag[1] == 'NNS': #tag 1 (2nd tag) is the pos tag
            #print(tag)
        if tag[0] not in stop_words:        #REMOVING STOP WORDS
            new_text.append(tag[0])

    print("\nOriginal")
    print(review)
    print("\nNew")
    print(" ".join(new_text))



