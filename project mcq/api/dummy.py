import requests
import re
import random
from pywsd.similarity import max_similarity
from pywsd.lesk import adapted_lesk
from nltk.corpus import wordnet 
from find_sentances import extract_sentences
import nltk
import pandas as pd
def conceptnet_distractors(word):
    print("6.Obtaining relative options from ConceptNet...")
    word = word.lower()
    word= word
    if (len(word.split())>0):
        word = word.replace(" ","_")

    response = {
            "@context": [
                "http://api.conceptnet.io/ld/conceptnet5.7/context.ld.json"
            ],
            "@id": "/c/en/example",
            "edges": [...],
            "view": {
                "@id": "/c/en/example?offset=0&limit=20",
                "firstPage": "/c/en/example?offset=0&limit=20",
                "nextPage": "/c/en/example?offset=20&limit=20",
                "paginatedProperty": "edges"
            }
            }
    distractor_list=[edge for edge in response["edges"]]
    return distractor_list

print(conceptnet_distractors("America"))
