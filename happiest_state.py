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

def getstate(tweet): # here we are extracting the place information of the tweet
    if 'place' in tweet and tweet['place'] is not None: # here we are checking if the place information is there.
        place = tweet['place']
        if 'full_name' in place: # here we are checking if the place's full name is there.
            full_name = place['full_name']
            if ', ' in full_name: # here it will check if the full name with comma where city folloewd by state or country.
                return full_name.split(', ')[1] # here it will return the place information
    return None # it returns the none where the place information is not found.

def main():
    sentifile = sys.argv[1] # it is the path for sentimental file which contains score
    tweetfile = sys.argv[2] # here it is the path for file which contains tweet
    
    sc1 = loadSentiScore(sentifile)
    
    statesentiment = {} #it is the intial dictionary where for storing the sentiment scores
    statecount = {}# it is the intial dictionary where for storing the number of the tweets
    
    with open(tweetfile, 'r') as afinnfile: # it reads the tweets file for processing data.
        for line in afinnfile:
            tweet = json.loads(line) # here it will parse the each line as the JSON object
            state = getstate(tweet) #it will extract the state from the tweet
            if state: # if the inforation of state is there.
                sentiment = calSenti(sc1, tweet)# here it will calculate the sentiment score
                statesentiment[state] = statesentiment.get(state, 0) + sentiment # here it increment the sentiment according to the state.
                statecount[state] = statecount.get(state, 0) + 1 # here the tweet count increment according to the state
    
    state_avgsentiment = {state: statesentiment[state] / statecount[state] for state in statesentiment} # it will calculate the average sentiment score according the the state.
    
    happiest_state1 = max(state_avgsentiment, key=state_avgsentiment.get) # it will find the happiest state with highest average sentiment scores
    print(happiest_state1) # here it will print the happiest state
    with open('happiest_state.txt', 'w',encoding='utf-8') as op:
            op.write(str(happiest_state1)) # here it contains the file with happiest state
    

if __name__ == '__main__':
    main() # it the main function which execute the program