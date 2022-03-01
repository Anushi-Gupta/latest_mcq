from summarizer import TransformerSummarizer

def Summary(text):
    model=TransformerSummarizer(transformer_type="XLNet",transformer_model_key="xlnet-base-cased")
    result = model(text, min_length=60,max_length=500,ratio=0.4)
    summary = "".join(result)
    return summary
'''with open("test_data.txt",encoding="utf8") as text_data:
    data=text_data.read()
print(Summary(data))
print("original length:-",len(data))
print("processed length:-",len(Summary(data)))'''





