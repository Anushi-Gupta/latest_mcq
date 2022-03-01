from bms.get_question import *
from bms.extract_data import *

def extract_boolean_question(text_data):
    boolean_question=[]
    for x in text_data[0].split("."):
        b_q=generate_question(x)
        boolean_question.extend(b_q["Boolean Questions"])
    print("Boolean Question")
    for x in range(1,len(boolean_question)):
        print(str(x)+").",boolean_question[x])
        
    return boolean_question



    