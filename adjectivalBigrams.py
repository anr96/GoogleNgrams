import os

#Example code for parsing the ngram files

class WN:
    def main(bigram_file):
        dictionary = []
        adj_bi_gram = []
        uniqueDictionary = {}

        adjTotal = 0
        counter = 0
        uniqueCounter = 0

        dictionary_file = open(os.path.expanduser('~/Documents/dictionary.txt'), 'r')
        df_lines = dictionary_file.readlines()
        for phrase in df_lines:
            dictionary.append(phrase.split()[0])
        dictionary_file.close()

        for bigram in bigram_file:
            #print (bigram.lower().split()[0] + "   " + bigram.lower().split()[1])
            if (bigram.lower().split()[0] in dictionary) and (bigram.lower().split()[1] in dictionary):
                adj_bi_gram.append(bigram)

        for i in adj_bi_gram:
            print(i)
            adjTotal += 1
        print(adjTotal)

    # dictionary containing single instances of the adj bigram and the count of times it appeared
    # the unique bigrams are the keys and the value they unlock is the counter
        for i in adj_bi_gram:
            bigram = i.lower().split()[0] + " " + i.lower().split()[1]
            # print bigram
            if bigram in uniqueDictionary:
                pass
            else:
                # set the counter back to 0 for each new adj bigram
                counter = 0
            counter += 1
            uniqueDictionary[bigram] = counter

        for i in uniqueDictionary:
            print(i, ":", uniqueDictionary[i])
            uniqueCounter += 1
        print(uniqueCounter)

    if __name__ == '__main__':
	# Example of ngram files from Google
        zy = open(os.path.expanduser('~/Documents/googlebooks-eng-all-2gram-20120701-zy'), 'r')
        zz = open(os.path.expanduser('~/Documents/googlebooks-eng-all-2gram-20120701-zz'), 'r')
        hx = open(os.path.expanduser('~/Documents/googlebooks-eng-all-2gram-20120701-hx'), 'r')
        aj = open(os.path.expanduser('~/Documents/googlebooks-eng-all-2gram-20120701-aj'), 'r')

        main(zy)
