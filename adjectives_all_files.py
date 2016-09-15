import os

class WN:	

	def main(bigram_file): 
		fileList = []	
		dictionary = []
		adj_bi_gram = []

		count = 0
		total = 0
		adjTotal = 0
		

		adj_file = open(os.path.expanduser('~/Documents/adj.txt'),'r')
		af_lines = adj_file.readlines()
		for phrase in af_lines: 
			fileList.append(phrase.split()[0])
			count += 1
		adj_file.close()
		#print fileList


		index_file = open(os.path.expanduser('~/Documents/index.txt'),'r')
		if_lines = index_file.readlines()
		for phrase in if_lines:
			fileList.append(phrase.split()[0])
			count += 1
		index_file.close()
		# print fileList
		

		print "Total of terms in dictionary (with repeats): "
		print count 

		for i in fileList:
			if i in dictionary:
				pass
			else:
				dictionary.append(i)
				total +=1
		print "Total of terms in dictionary (without repeats):"
		print total
		print
		
		for bigram in bigram_file: 
			#print bigram
			# print bigram.lower().split()[0] + "   " + bigram.lower().split()[1]
			if (bigram.lower().split()[0] in dictionary) and (bigram.lower().split()[1] in dictionary) :
				#print "Adjectival bigram: " + bigram
				adj_bi_gram.append(bigram)


		print "FINISHED COMPARING"
		print "These are the adjectival bigrams"
		for i in adj_bi_gram:
			print i	
			adjTotal += 1
		print "the total of adjectival bigrams in this file is: "
		print adjTotal
			
	if __name__ == '__main__':
		#a_ = open(os.path.expanduser('~/Documents/googlebooks_bigrams_a_'),'r')
		#aa = open(os.path.expanduser('~/Documents/googlebooks_bigrams_aa'),'r')
		cc = open(os.path.expanduser('~/Documents/googlebooks_bigrams_cc'),'r')
		#zi = open(os.path.expanduser('~/Documents/googlebooks_bigrams_zi'),'r')
		#main(aa)
		main(cc)
		#main(zi)
		
		

 	

