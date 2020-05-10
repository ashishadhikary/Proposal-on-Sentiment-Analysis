#  Data cleaning process
# removing the punctuation,change all words to lowercase

import string
import nltk
from collections import Counter
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd

random_text=input("Enter the sentiment/sentence to be analysed \n")
File1=open("readfile.txt",'w')
File1.write(random_text)
File1.close()



text=open('readfile.txt',encoding='utf-8').read()
#print(text)

# Defining the function to remove punctutation
def remove_punctuation(txt):
    txt_nopunct="".join([c for c in txt if c not in string.punctuation])
    return txt_nopunct


#converting the words into lowercase
lowercase=text.lower()

#removing the punctuation in the lowercase

no_punct=remove_punctuation(lowercase)
    #print(no_punct)

# For tokenization
tokenized_words=no_punct.split();
print(tokenized_words)

# Removing the stop words
# stop words are like: i ,the,we,this,it etc
# we need to import "nltk" packages for stopwords
stopwords=nltk.corpus.stopwords.words('english')

def remove_stopwords(txt):
    no_stopwords=[word for word in txt if word not in stopwords]
    return no_stopwords

no_stop_words=remove_stopwords(tokenized_words)
#print(no_stop_words)

# For emotion file
emotion_list=[]
# emotion.txt file contains list of words with its respective emotion
# It contains only around 600 words.The more words it has the more accuracy the result.
with open('emotion.txt','r') as file:
    for line in file:
        # if we print line then the output contain some new line so we need to remove it
        clear_line=line.replace('\n','').replace(',','').replace("'","").strip()
        #print(clear_line)
        word,emotion=clear_line.split(':')
        # It splits in two words.
        #print("Word:" +word + " "+ "Emotion:" +emotion)

        if(word in no_stop_words):
            emotion_list.append(emotion)
print("Printing emotion listes")
print(emotion_list)

# For counting the different emotion numbers individually
W=Counter(emotion_list)
print(W)

# for sentiment anlysis(main part)
# it contains the score about positive,negative on the text

def sentiment_analysis(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    # print(score)
    neg = score['neg']
    pos = score['pos']
    if neg > pos:
        print("Sentiment is negative")
    elif pos > neg:
        print("Sentiment is positive")
    else:
        print("Sentiment is neutral")

# We need to pass the text file insted of words(tokinezed)
sentiment_analysis(no_punct)

plt.bar(W.keys(),W.values())
plt.savefig('graph.png')
plt.show()



