import sys
import json
from collections import defaultdict

def comTermfreq(tweet_file):# here the function will calculate the frequency of word ibn the tweet.
    termcount = defaultdict(int) # here we will initial defaultdict for storing the each term 
    tterms = 0
    
    with open(tweet_file, 'r') as afinnfile:# it reads the tweets file for processing data.
        for line in afinnfile:
            tweet = json.loads(line)# here it will parse the each line as the JSON object
            if 'text' in tweet:
                words = tweet['text'].split()# we will split the text into the individual words
                for word in words:
                    termcount[word] += 1 # here it will increment the count for the words
                    tterms += 1 # here we increment thr count for the total number of the terms.
    
    term_frequency = {term: count / tterms for term, count in termcount.items()} # it will calculate the term frequency by the each term count by number of terms.
    
    return term_frequency # it will term frequency

def main():
    tweetfile = sys.argv[1] # here it is the path for file which contains tweet
    termfrequency = comTermfreq(tweetfile) # here term frequency done by the ComTermfreq function
    
    for term, frequency in termfrequency.items():
        print(f"{term} {frequency}") # it will print the term and frequency

    with open('frequency.txt', 'w',encoding='utf-8') as op:
        for term, frequency in termfrequency.items():
            op.write(f"{term} {frequency}\n") # it will have output file which contains the term and frequency

if __name__ == '__main__':
    main() # it the main function which execute the program