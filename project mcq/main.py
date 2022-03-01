from flask import Flask,render_template,request,jsonify,flash,redirect

from api.gen_mcq import display

import pandas as pd
import json
from bms.boolean import *
from bms.one_word import *
from bms.extract_data import extraction_text,extraction1_text
from api.find_sentances import extract_sentences

app=Flask(__name__)

@app.route("/home")
def first_page():
    return render_template("index.html")

@app.route("/get_mq/",methods=["POST"])
def get_mcqq():
    try:
        text_data=request.files["file"]
        text_data.save(text_data.filename)
        print(1)
        if text_data.filename.split(".")[-1]=="txt":
            print(text_data.filename)
            print(2)
            text_data=extraction_text(text_data.filename)
            print(text_data)
            text_data=display(text_data,quantity="high")
            text_data=pd.DataFrame(text_data)
            print(3)
            text_data=text_data.to_json(orient='records')
            print(4)
            req_dict={}
            for i,j in json.loads(text_data):
                req_dict.update({f"Question{i}:-":j['question'],f"options{i}":j['options'],f"answer{i}":j['answer']})
                
                
            
            return jsonify({"results":req_dict})
            
    except Exception as e:
        with open("response1.json") as text:
            text_data=text.read()
        
        return jsonify(text_data)

@app.route("/get_boolean/",methods=["POST"])
def bool_qstn():
    try:
        text_data=request.files["file"]
        if text_data.filename !="":
            text_data.save(text_data.filename)
        if text_data.filename.split(".")[-1]=="txt":
    
            text_data=extraction1_text(text_data.filename)
            print(2)
            text_data=extract_boolean_question(text_data)
            print(3)
            return jsonify({"results":text_data})
    except Exception as e:
        return f"Select the correct file format:-{e}"   
        
@app.route("/get_one_word/",methods=["POST"])
def oneword_qstn():
    try:
        text_data=request.files["file"]
        if text_data.filename !="":
            text_data.save(text_data.filename)
        if text_data.filename.split(".")[-1]=="txt":
    
            text_data=extraction1_text(text_data.filename)
            text_data=mcq_quest(text_data)
            return jsonify({"results":text_data})
    except Exception as e:
        return f"Select the correct file format:-{e}"
        

if __name__=="__main__":
    app.run(host="127.0.0.1",debug=True)