import os

"""
This program determines that if both words of the bigram in the desired input file are found in the
English adjectives dictionary, the bigram and its metadata will be added to a list of adjectival bigrams
A dictionary of unique adjectival bigrams is subsequently created from the adjectival bigrams list {bigram : occurrences}
"""


class LingClass(object):

    # lists for English adjectives and adjectival bigrams, dictionary for unique terms & their count
    dictionary = []
    adj_bigram = []
    unique_dictionary = {}

    # counter variables
    adj_total = 0
    counter = 0
    unique_counter = 0

    # open bigram file and open the two files that the results will be written to
    def __init__(self, bigram_file_name):
        self.bigram_file_name = bigram_file_name
        self.bigram_file = open(os.path.expanduser('~/Documents/googlebooks-eng-all-2gram-20120701-%s' % bigram_file_name), 'r')
        self.nonunique_output = open(os.path.expanduser('~/Documents/%s_results_both' % bigram_file_name), 'w')
        self.unique_output = open(os.path.expanduser('~/Documents/%s_unique' % bigram_file_name), 'w')
        self.open_dictionary()

    # opens dictionary of adjectives
    def open_dictionary(self):
        dictionary_file = open(os.path.expanduser('~/Documents/clean_dictionary.txt'), 'r')
        df_lines = dictionary_file.readlines()
        for phrase in df_lines:
            self.dictionary.append(phrase.split()[0])
        dictionary_file.close()
        self.check_if_bigram()

    # if both words in the bigram are in the adjective dictionary, add them to the proper list
    def check_if_bigram(self):
        for bigram in self.bigram_file:
            if (bigram.lower().split()[0] in self.dictionary) and (bigram.lower().split()[1] in self.dictionary):
                self.adj_bigram.append(bigram)
        self.non_unique_bigram_list()

    # write to file the list of adjectival bigrams and total of unique/non-unique phrases
    def non_unique_bigram_list(self):
        for i in self.adj_bigram:
            self.nonunique_output.write(i)
            print(i)
            self.adj_total += 1
        print(self.adj_total)
        self.nonunique_output.write("\n\nTotal of adjectival bigrams: ")
        self.nonunique_output.write(str(self.adj_total) + "\n")
        self.unique_bigram_list()

    # write to file only unique items and the total times that phrase occurred
    def unique_bigram_list(self):
        for i in self.adj_bigram:
            bigram = i.lower().split()[0] + " " + i.lower().split()[1]
            if bigram in self.unique_dictionary:
                pass
            else:
                # set the counter back to 0 for each new adj bigram
                self.counter = 0
            self.counter += 1
            self.unique_dictionary[bigram] = self.counter

        for i in self.unique_dictionary:
            print(i, ":", self.unique_dictionary[i])
            self.unique_output.write(str(i) + ": " + str(self.unique_dictionary[i]) + "\n")
            self.unique_counter += 1
        print(self.unique_counter)

        self.nonunique_output.write("Total of unique bigrams: ")
        self.nonunique_output.write(str(self.unique_counter))
        self.nonunique_output.close()

        self.unique_output.write("\nTotal of unique bigrams: ")
        self.unique_output.write(str(self.unique_counter))
        self.unique_output.close()


file_name = input("Enter a bigram file to be parsed:\n")
file = LingClass(file_name)




