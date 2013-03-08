'''
    Dictionary based WSD
    Author: Herat Gandhi
'''

import nltk
from nltk.corpus import stopwords
from nltk.corpus import wordnet
import string
import re

'''
    Function to get context words from the given sample
    @param line: Sample from which we need to retrieve context words
    @param n: n context words we want to retrieve
    @return: Return list of n context words
'''
def get_context_words(line,n,lines1):
    temp = line.lower()
    temp = re.sub('[0-9]+','',temp)
    
    first_at = temp.find('@')
    last_at = temp.rfind('@')+1
    
    temp1 = temp[:first_at]
    temp2 = temp[last_at:]
    
    for punct in string.punctuation:
        temp1 = temp1.replace(punct,'')
        temp2 = temp2.replace(punct,'')
    
    temp_l1 = temp1.split()
    temp_l2 = temp2.split()
    
    important_words1 = filter(lambda x: x not in stopwords.words('english'), temp_l1)
    important_words1 = filter(lambda x: x not in lines1, important_words1)
    important_words2 = filter(lambda x: x not in stopwords.words('english'), temp_l2)
    important_words2 = filter(lambda x: x not in lines1, important_words2)
    
    important_words1 = nltk.pos_tag(important_words1)
    important_words2 = nltk.pos_tag(important_words2)

    if len(important_words1) > n:
        temp_words1 = important_words1[len(important_words1)-n:]
    else:
        temp_words1 = important_words1
    temp_words2 = important_words2[:n]
    
    senses = []
    '''wnl = nltk.WordNetLemmatizer
    for t in temp_words1:
        #senses.append(wordnet.Synset())
        senses.append(wordnet.synset('dog.n.01'))'''
    dog = wordnet.synset('dog.n.01')
    hyp = lambda s:s.hypernyms()
    print(list(dog.closure(hyp)));
    
    #print(senses)
    return ''

'''
    Function to perform WSD based on dictionaries
    @param filename: Filename to be used for testing
'''
def WSD_Dict(filename):
    fp = open(filename,'r')
    lines = fp.readlines()
    fp2 = open('words.txt','r')
    lines1 = fp2.read().splitlines()
    
    for line in lines:
        at_p = line.find('@') #Find first occurance of @ that helps to identify where to break string
        starting = line [:at_p].split()
        strating_target = starting[0].split('.')[0] #Target word to be disambiguated
        form = starting[0].split('.')[1] #Target word form
        line = line[at_p+1:] #Get rest of the line
        target_in_sentence = line[line.find('@')+1:line.rfind('@')] #Target word in the sentence
        #line = line.replace('@','')
        context_words = get_context_words(line,5,lines1)
    
def main():
    filename = raw_input('Enter file name to test: ')
    WSD_Dict(filename)

main()