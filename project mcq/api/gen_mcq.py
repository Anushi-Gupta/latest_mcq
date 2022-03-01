import requests
import re
import random
from pywsd.similarity import max_similarity
from pywsd.lesk import adapted_lesk
from nltk.corpus import wordnet 
from api.find_sentances import extract_sentences
import nltk
import pandas as pd
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('stopwords')


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

    
def display(text,quantity):
    
    filtered_sentences = extract_sentences(text,quantity)
    
    options_for_mcq = {}
    for keyword in filtered_sentences:
        wordsense = word_sense(filtered_sentences[keyword][0],keyword)
        if wordsense:
           distractors = wordnet_distractors(wordsense,keyword) 
           if len(distractors)>0:
                options_for_mcq[keyword]=distractors
           if len(distractors)<4:
               distractors = conceptnet_distractors(keyword)
               if len(distractors)>0:
                    options_for_mcq[keyword]=distractors
                    
        else:
            distractors = conceptnet_distractors(keyword)
            if len(distractors)>0:
                options_for_mcq[keyword] = distractors
    print("7. Creating JSON response for API...")
    df = pd.DataFrame()
    cols = ['question','options','extras','answer']
    
    index = 1
    print ("**********************************************************************************")
    print ("List of MCQ generated:-")
    print ("************************************************************************************\n\n")
    for i in options_for_mcq:
        sentence = filtered_sentences[i][0]
        sentence = sentence.replace("\n",'')
        pattern = re.compile(i, re.IGNORECASE)
        output = pattern.sub( " ______ ", sentence)
        print ("%s)"%(index),output)
        options = [i.capitalize()] + options_for_mcq[i]
        top4 = options[:4]
        random.shuffle(top4)
        optionsno = ['a','b','c','d']
        for idx,choice in enumerate(top4):
            print ("\t",optionsno[idx],")"," ",choice)
        print ("\nMore options: ", options[4:8],"\n\n")
        df = df.append(pd.DataFrame([[output,top4,options[4:8],i.capitalize()]],columns=cols))
        index = index + 1         
    df_data=df.copy()  
    
    df.to_json('response1.json',orient='records',force_ascii=False)
    return df_data

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
'''with open("test_data.txt",encoding="utf8") as text_data:
    data=text_data.read()
display(data,quantity="high")'''
    
