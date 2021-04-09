
import numpy as np
from nltk.tokenize.treebank import TreebankWordDetokenizer

"""
	First run this from AllenNLP 2.0 main program : 
    
    #read in text
	text = open("yourtext.txt").read()
	
	#initialize predictor for coref resolution, form prediction

	predictor = Predictor.from_path("https://storage.googleapis.com/allennlp-public-models/coref-spanbert-large-2021.03.10.tar.gz")
	prediction = predictor.predict(document=text)

	# write to csv and .npy

	w = csv.writer(open("output.csv", "w"))	
	for key, val in prediction.items():
		w.writerow([key, val])

	f = open("dict.txt","w")
	f.write( str(prediction) )

	f.close()

	np.save('first_grade.npy', prediction) 

"""




# path: file path to .npy file holding coreference information


def( path: str): -> str

	# read in dictionary
	read_dictionary = np.load(path,allow_pickle='TRUE').item()
	clusters = read_dictionary["clusters"]
	doc = read_dictionary["document"]

	flat_cluster_lista = [item for sublist in read_dictionary['clusters'] for item in sublist]
	flat_cluster_listb = [item for sublist in flat_cluster_lista for item in sublist]

	alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

	dict_tex = {}
	for k,cluster in enumerate(clusters):
	    for i,instance in enumerate(cluster):
	        for j,word in enumerate(instance):
	            dict_tex[instance[j]] = "[" + doc[word] + "$]_{" + alphabet[j] + "}^{" + str(k) + "}$"


	full_tex = []

	for i,word in enumerate(doc):
	    if i in flat_cluster_list:
	        full_tex.append(dict_tex[i])
	    else:
	        full_tex.append(word)



	full_tex_untokenized = TreebankWordDetokenizer().detokenize(full_tex)

	return full_tex 


# Results can be directly copy and pasted into overleaf
