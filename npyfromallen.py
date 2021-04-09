import allennlp

#import networkx as nx
from allennlp.predictors.predictor import Predictor
import allennlp_models.tagging
import csv
import numpy as np


if __name__ == "__main__":
	
	#insert your text file path
	
	text = open("youtext.txt").read()
	      
	
	predictor = Predictor.from_path("https://storage.googleapis.com/allennlp-public-models/coref-spanbert-large-2021.03.10.tar.gz")
	prediction = predictor.predict(document=text)

	print(predictor.top_spans)
	w = csv.writer(open("output.csv", "w"))	
	for key, val in prediction.items():
		w.writerow([key, val])

	f = open("dict.txt","w")
	f.write( str(prediction) )

	f.close()

	np.save('first_grade.npy', prediction) 

   

