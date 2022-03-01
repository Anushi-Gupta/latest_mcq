def extraction_text(sample_data):
    with open(sample_data,encoding="utf8") as text_data:
        text_data=text_data.read()
    return text_data
def extraction1_text(sample_data):
    with open(sample_data,encoding="utf8") as text_data:
        text_data=text_data.read()
    n=1024 
    text_data=[text_data[i:i+n] for i in range(0,len(text_data),n)]
    return text_data


    