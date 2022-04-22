import numpy as np


class Tf_idf_encoder:

    def __init__(self, data):
        self.data = data
        self.N = len(self.data)

    """This function is going to create a list of sentences from the file that will be used 
    to tokenize the document"""

    def document_corpus(self):
        sentences_list = []
        for row in range(len(self.data)):
            sentences_list.append(self.data.iloc[row])
        return sentences_list

    """This function has a task of creating the set of words which are unique and will help to
    compute the number of documents where these words are contained in.
    """

    def corpus(self):
        Corpus = set()
        for content in self.document_corpus():
            for word in content.split():
                if word not in Corpus:
                    Corpus.add(word)
        return Corpus

    """If we need to pick any sentence from the file, we will give index to the function and picks the sentence at 
    that index from sentences document """

    def pick_sentence(self, index):
        return self.document_corpus()[index]
        # picking word in corpus

    def pick_word(self, index, word_loc):
        word_loc = list(word_loc)
        word_selected = map(self.pick_sentence(index).split().__getitem__, word_loc)
        return list(word_selected)

    """This function is for creating a dictionary of the words from corpus as key and their re
    -petition in in a whole """

    def vocabular_index(self):
        # Creating an index for each word in our vocab.
        index_dict = {}  # Dictionary to store index for each word
        i = 0
        for word in self.corpus():
            index_dict[word] = i
            i += 1
        return index_dict

    """This function is for computing the number of document that
     contains the word. The output is the dictionary.
     -------------------------------------------------
     ** Each word from corpus will be taken as dictionary key.
     **Each value of dictionary will be corresponding to the number of document that contains
     a given word.
     This function will be usefully for final computation of td_idf.
     """

    def total_doc_contain_word(self, document):
        word_frequency_per_sent_dic = {}
        for word in self.corpus():
            word_frequency_per_sent_dic[word] = 0
            for sentence in self.document_corpus():
                if word in document:
                    word_frequency_per_sent_dic[word] += 1
        return word_frequency_per_sent_dic

    """Function to recognize the accuracy of any word we need if the word exist in document"""

    def tf(self, word, document):
        N = len(document)
        frequency = len([exist_ for exist_ in document if exist_ == word])
        return frequency / N

    """This function will be computing the value for log(N/N_if)
    ------------------------------------------------------------
    N: is total number of documents.
    N_if: is the number of documents that contains a given word.
    Here the values of dictionary provided by total_doc_contain_word function are that N_if
    """

    def idf(self, word):
        total_doc = len(self.document_corpus())

        try:
            word_count = self.total_doc_contain_word()[word] + 1
        except:
            word_count = 1
        return np.log(total_doc / word_count)

    """ This function is the last one for final encoding document using td_idf, the output will
    be the matrix arrays of weights corresponding to any specific word"""

    def tf_idf(self, sentence):
        tf_idf_vector = np.zeros((len(self.corpus()),))
        for word in sentence:
            tf = self.tf(word, sentence)
            idf = self.idf(word)
            weight = tf * idf
            tf_idf_vector[self.vocabular_index()[word]] = weight
            return tf_idf_vector
