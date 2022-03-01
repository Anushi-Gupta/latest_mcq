from nltk.tokenize import sent_tokenize
from flashtext import KeywordProcessor 
from api.extract_keywords import final_keywords
from api.generate_summary import Summary


def set_sentances(text):
    sentences = [sent_tokenize(text)]
    sentences = [i for sent in sentences for i in sent]
    
    sentences = [sent.strip() for sent in sentences if len(sent)>20]
    return sentences


def extract_sentences(text,quantity):
    keywords,text = final_keywords(text,quantity)
    key_processor = KeywordProcessor()
    filtered_sentences = {}
    
    for i in keywords:
        filtered_sentences[i]=[]
        key_processor.add_keyword(i)
        
    sentences = set_sentances(text)
    print("4.Filtering sentences...")
    for sent in sentences:
        keyword_searched = key_processor.extract_keywords(sent)
        for key in keyword_searched:
            filtered_sentences[key].append(sent)
    filtered_sentences = dict([(key,val) for key,val in filtered_sentences.items() if(val)])
    
    for i in filtered_sentences.keys():
        values = filtered_sentences[i]            
        values = sorted(values,key=len,reverse=True)
        filtered_sentences[i] = values
        
    print(filtered_sentences)
    return filtered_sentences
    
'''with open("test_data.txt",encoding="utf8") as text_data:
    text_data=text_data.read()
print(extract_sentences(Summary(text_data),quantity="high"))'''
    