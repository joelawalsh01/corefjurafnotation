
import numpy as np
from nltk.tokenize.treebank import TreebankWordDetokenizer

"""
	First run npyfromallen.py
    
  
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

	return full_tex_untokenized 


# Results can be directly copy and pasted into overleaf
