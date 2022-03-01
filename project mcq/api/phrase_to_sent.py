from keytotext import pipeline
nlp = pipeline("k2t-base")  
params = {"do_sample":True, "num_beams":4, "no_repeat_ngram_size":3, "early_stopping":True}   
print (nlp(['Delhi', 'India', 'capital'], **params)) 