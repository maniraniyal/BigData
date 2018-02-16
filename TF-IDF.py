'''
Created on 2018-02-15

@author: mani
'''
import sys,os
import glob
import collections
import math
from functools32 import lru_cache
from multiprocessing import Pool

CORPUS = {}
TOTAL_DOCS = 0
def TF(term,doc):
    if doc in CORPUS.keys():
        if CORPUS[doc][term]:
            return float(CORPUS[doc][term])/float(TOTAL_DOCS)
        else:
            return 0
    return 0
def IDF(term):
    return math.log(float(TOTAL_DOCS)/len(search_doc_with_term(term)))
def TF_IDF(term,doc):
    tf = TF(term,doc)
    idf = IDF(term)
    return tf*idf
def create_count(text):
    text = text.lower()
    split_data = text.split(" ")
    count_dict = collections.Counter(split_data)
    return count_dict

def search_doc_with_term(term):
    tmp = []
    for f, dic in CORPUS.iteritems():
        if term in dic.keys():
            tmp.append(f)
    return tmp

def load_corpus(dirc):
    global CORPUS
    global TOTAL_DOCS
    for d in dirc:
        for filename in glob.glob(d+'/*'):
            if os.path.isfile(filename):
                with open(filename) as fd:
                    CORPUS[filename] = create_count(fd.read())
    TOTAL_DOCS = len(CORPUS)
@lru_cache(maxsize=1024)
def search_term(term,top=10):
    search_result = []
    for doc in CORPUS.keys():
        result = TF_IDF(term, doc)
        search_result.append(tuple([doc,result]))
    search_result.sort(key=lambda x:x[1],reverse=True)
    return search_result[:top]
def test_create_count():
    tmp = None
    with open("review_polarity/txt_sentoken/pos/cv000_29590.txt") as fd:
        tmp = fd.read()
    for i,v in create_count(tmp).iteritems():
        print i,v
    sys.exit()
    
if __name__ == '__main__':
    #test_create_count()
    if len(sys.argv) < 2:
        print "Please provide input directory!"
        print "Usage: TF-IDF.py [dir1] [dir2] ..."
        sys.exit()
    else:
        for d in sys.argv[1:]:
            if os.path.isdir(d):
                pass
            else:
                print d," is not a directory!"
                sys.exit()
    
    
    load_corpus(sys.argv[1:])
    print "Total documents in the Corpus:",len(CORPUS.keys())
    while True:
        term = raw_input("Please enter the Term to search in the Corpus:")
        result = search_term(term.lower())
        for res in result:
            #print chr(27) + "[2J"
            print res[1],res[0]
    
    
