import sys
import json
from collections import defaultdict, Counter

def get_htag(tweet): # the function is for extracting the hastag from the tweets
    htags = [] # here we will intailize the list for storing the hastags
    if 'entities' in tweet and 'hashtags' in tweet['entities']: # here it will check if the tweets having the entities and hastag fields.
        for htag in tweet['entities']['hashtags']:
            htags.append(htag['text']) # it will append the text of the hashtag into the list.
    return htags # it will return the hashtags

def main():
    tweet_file = sys.argv[1] # here it is the path for file which contains tweet
    
    htag_count = defaultdict(int) # here it will initialize the defaultdict to store the count of each hastag
    
    with open(tweet_file, 'r') as afinnfile: # it reads the tweets file for processing data.
        for line in afinnfile:
            tweet = json.loads(line)# here it will parse the each line as the JSON object
            htags = get_htag(tweet) # here it will extract the hastag
            for htag in htags:
                htag_count[htag] += 1 # here it have increment according to the hastag count
    
    top_ten = Counter(htag_count).most_common(10) # it will have count and  have 10 most common hastags.
    
    for htag, count in top_ten:
        print(f"{htag} {count}") # it will print the top 10 common hashtags.

    with open('top_ten.txt', 'w',encoding='utf-8') as op:
        for htag, count in top_ten:
            op.write(f"{htag} {count}\n") # it will generate the top 10 common hashtags in output file.

if __name__ == '__main__':
    main() # it the main function which execute the program