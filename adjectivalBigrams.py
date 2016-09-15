import os

class WN:	

	def main(bigram_file): 
		fileList = []	
		dictionary = []
		adj_bi_gram = []

		adjTotal = 0
		
		# The adjectives in adj.txt & index.txt are added into fileList
		# Only the first term of each line is necessary
		adj_file = open(os.path.expanduser('~/Documents/adj.txt'),'r')
		af_lines = adj_file.readlines()
		for phrase in af_lines: 
			fileList.append(phrase.split()[0])
		adj_file.close()


		index_file = open(os.path.expanduser('~/Documents/index.txt'),'r')
		if_lines = index_file.readlines()
		for phrase in if_lines:
			fileList.append(phrase.split()[0])
		index_file.close()
		

		
		#Discard of repeats from fileList and entered into dictionary
		for i in fileList:
			if i in dictionary:
				pass
			else:
				dictionary.append(i)

		#Determines if both terms in the bigram are adjectives
		for bigram in bigram_file: 
			if (bigram.lower().split()[0] in dictionary) and (bigram.lower().split()[1] in dictionary) :
				adj_bi_gram.append(bigram)


		print "A list of adjectival bigrams: "
		for i in adj_bi_gram:
			print i	
			adjTotal += 1
		print "the total of adjectival bigrams in this file is: "
		print adjTotal
			
	if __name__ == '__main__':
		#Google Files found at http://storage.googleapis.com/books/ngrams/books/datasetsv2.html

		#a_ = open(os.path.expanduser('~/Documents/googlebooks_bigrams_a_'),'r')
		#aa = open(os.path.expanduser('~/Documents/googlebooks_bigrams_aa'),'r')
		cc = open(os.path.expanduser('~/Documents/googlebooks_bigrams_cc'),'r')
		#zi = open(os.path.expanduser('~/Documents/googlebooks_bigrams_zi'),'r')
		#main(a_)
		#main(aa)
		main(cc)
		#main(zi)
		
		

 	

