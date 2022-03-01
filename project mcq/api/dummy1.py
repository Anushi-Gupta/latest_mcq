import requests
import re
import random
from pywsd.similarity import max_similarity
from pywsd.lesk import adapted_lesk
from nltk.corpus import wordnet 
from find_sentances import extract_sentences
import nltk
import pandas as pd
def word_sense(sentence,keyword):
    print("5.Getting word sense to obtain best MCQ options with WordNet...")
    word = keyword.lower()
    if len(word.split())>0:
        word = word.replace(" ","_")
    
    syon_sets = wordnet.synsets(word,'n')
    if syon_sets:
        try:
            wup = max_similarity(sentence, word, 'wup', pos='n')
            adapted_lesk_output =  adapted_lesk(sentence, word, pos='n')
            lowest_index = min(syon_sets.index(wup),syon_sets.index(adapted_lesk_output))
            return syon_sets[lowest_index]

        except:
            return syon_sets[0]
           
    else:
        return None

   
    

print(word_sense("Ilive in America","America"))
