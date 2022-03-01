import requests
import re
import random
from pywsd.similarity import max_similarity
from pywsd.lesk import adapted_lesk
from nltk.corpus import wordnet 
from find_sentances import extract_sentences
import nltk
import pandas as pd

def wordnet_distractors(syon,word):
    print("6.Obtaining relative options from Wordnet...")
    distractors = []
    word = word.lower()
    ori_word = word
    
    if len(word.split())>0:
        word = word.replace(" ","_")
        
    hypersyon = syon.hypernyms()
    if(len(hypersyon)==0):
        return distractors
    for i in hypersyon[0].hyponyms():
        name = i.lemmas()[0].name()
        
        if(name==ori_word):
            continue
        name = name.replace("_"," ")
        name = " ".join(i.capitalize() for i in name.split())
        if name is not None and name not in distractors:
            distractors.append(name)
    return distractors

print(wordnet_distractors("Africa","America"))