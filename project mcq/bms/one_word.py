from bms.get_question import *
from bms.extract_data import *
def mcq_quest(text_data):
    mcq_question=[]
    for i in text_data[0].split("."):
        mcq_q=generate_one_word(i) 
        mcq_question.append(mcq_q)
        
    return mcq_question

'''with open("test_data.txt",encoding="utf8") as text_data:
    text_data=text_data.read()
n=1024 
text_data=[text_data[i:i+n] for i in range(0,len(text_data),n)]
print(mcq_quest(text_data))'''