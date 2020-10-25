import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
import re

class Preprocess:
    trig = []
    def __init__(self,filename):
         init_token = self.openFile(filename)
         clean_token = self.clean(init_token)
         trig_list = self.makeTrig(clean_token)
         #store in text file
         #store(trig_list)
         self.trig = trig_list
         
    def openFile(self,filename):
        f=open(filename,"r")
        orig=f.read().replace("\n"," ")
        orig = re.sub(r'[^\w\s]', '', orig)
        orig = re.sub(r'[0-9]+', '', orig)
        return word_tokenize(orig)

    def clean(self,init_token):
        #lowerCase
        tokens_o = [token.lower() for token in init_token]
        #stop word removal
        #punctuation removal
        stop_words=set(stopwords.words('english'))
        punctuations=['"','.','(',')',',','?',';',':',"''",'``']
        filtered_tokens = [w for w in tokens_o if not w in stop_words and not w in punctuations]
        return filtered_tokens

    def makeTrig(self,clean_token):
        trigrams=[]
        for i in range(len(clean_token)-2):
            t=(clean_token[i],clean_token[i+1],clean_token[i+2])
            trigrams.append(t)
        return trigrams
    #def print
'''
    def store(trig_list):
'''
