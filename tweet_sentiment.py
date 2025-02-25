import sys
import json

def loadSentiScore(sentifile):# here we are loading the file for sentiment scores
    sc1 = {} #intial dictionary for adding the sentiment scores
    with open(sentifile, 'r') as afinnfile:#here we are reading the file
        for line in afinnfile:
            term, score = line.split('\t') #it split the line into parts one is term and another is score
            sc1[term] = int(score) #here we are storing according to term and it's score in the dictionary
    return sc1 #it returns the sentiment scores

def calSenti(sc1, tweet):#here we are calculating the sentiment score according to the sentiment dictionary. 
    sentiment = 0
    if 'text' in tweet: # here we checking according to the tweets havinf the text
        words = tweet['text'].split() # we will split the text into the individual words
        for word in words:
            if word in sc1:# we are checking the word is present in the sentiment where data in dictionary.
                sentiment += sc1[word] # here we are incrementing the sentimental score
    return sentiment # it returns the sentimental score.

def main():
    sentifile = sys.argv[1] # it is the path for sentimental file which contains score
    tweetfile = sys.argv[2] # here it is the path for file which contains tweet
    
    sc1 =loadSentiScore(sentifile) # it will load the sentimental scores into the dictionary.
    
    with open(tweetfile, 'r') as afinnfile, open('tweet_sentiment.txt', 'w') as op: # read and write of tweet file with sentiment scores.
        for line in afinnfile:
            tweet = json.loads(line) # here it will parse the each line as the JSON object 
            sentiment = calSenti(sc1, tweet) # here it will calculate the sentiment scores according to the tweet
            print(sentiment) # here it will print the sentiment scores as output.
            op.write(f"{sentiment}\n") # here it will generate the output file with sentiment scores.





if __name__ == '__main__':
    main() # it the main function which execute the program.