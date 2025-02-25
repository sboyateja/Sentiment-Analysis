import sys
import json

def loadSentiScore(sentifile):# here we are loading the file for sentiment scores
    sc1 = {} #intial dictionary for adding the sentiment scores
    with open(sentifile, 'r') as afinnfile:#here we are reading the file
        for line in afinnfile:
            term, score = line.split('\t') #it split the line into parts one is term and another is score
            sc1[term] = int(score) #here we are storing according to term and it's score in the dictionary
    return sc1 #it returns the sentiment scores

def calTermSenti(sc1, tweets): # the function will calculate the sentiment score for the terms.
    termsentiment = {} # initial dictionary for the sentiment scores according to the terms 
    termcount = {} # intial dictionary for the count of occurence for the each term
    
    for tweet in tweets:
        if 'text' in tweet: # it will check the tweet is having text
            words = tweet['text'].split() # here it will split the text of tweet into the individual words
            tweet_sentiment = sum(sc1.get(word, 0) for word in words) # it will calculate the sentiment score for the tweet
            for word in words:
                if word not in sc1: # it will check the if the word is present in sentiment dictionary.
                    termsentiment[word] = termsentiment.get(word, 0) + tweet_sentiment # it will add the sentiment score of tweet for the terms cummulative score
                    termcount[word] = termcount.get(word, 0) + 1 # here the increment for the occurence count of term.
    
    for term in termsentiment: 
        termsentiment[term] = termsentiment[term] / termcount[term] # here we will calculate the average sentiment score for the each term
    
    return termsentiment #it will return theterm sentiment cores into the dictionary 

def main():
    sentifile = sys.argv[1] # it is the path for sentimental file which contains score
    tweetfile = sys.argv[2] # here it is the path for file which contains tweet
    
    
    sc1 = loadSentiScore(sentifile) # here it will load the sentiment score into the dictionary
    
    tweets = [] #intializing the list for storing tweets 
    with open(tweetfile, 'r') as afinnfile: # it reads the tweets file for processing data.
        for line in afinnfile:
            tweet = json.loads(line)# here it will parse the each line as the JSON object
            tweets.append(tweet) # it will add the tweet into the list
    
    termsentiment = calTermSenti(sc1, tweets) # here it wil calculate the sentiment scores for the terms
    
    for term, sentiment in termsentiment.items():
        print(f"{term} {sentiment}") # print the terms and the sentiment score

    with open('term_sentiment.txt', 'w',encoding='utf-8') as op:
        for term, sentiment in termsentiment.items():
            op.write(f"{term} {sentiment:.4f}\n") # it will generate the output file with term and sentiment score

if __name__ == '__main__':
    main()# it the main function which execute the program