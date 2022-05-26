import re
import numpy


class FrequencyEcoder:

    def __init__(self, data):
        """These data here has to be cleaned without those special symbols."""
        self.data = data

    """This function has task of computing the frequency of the word in each row of the file and returns the row as dictionary of word as key and 
    frequency as value.
    """

    def remove_char(text):
        clean = re.compile('<.*?>')
        return re.sub(clean, '', text)

    def frequency_computer(self, string):

        string = string.split()

        dict_freq = {}

        freq_list = []

        for i in string:
            if i not in freq_list:
                #             print(i)
                freq_list.append(i)
        for j in range(0, len(freq_list)):
            dict_freq[freq_list[j]] = string.count(freq_list[j])
        return dict_freq

    """This function is for changing each row of the file into dictionary words as keys and their repetitions as values. It will be usefully to
    the time of replacing the word by its total frequency in all file.
    """

    def row_to_dict(self):
        inputs = self.data
        for index, item in inputs.items():
            inputs[index] = self.remove_char(item).replace('br br', ' ')
            for _ in inputs[index]:
                if type(_) == int:
                    inputs[index] = item.replace('_', ' ')

            inputs[index] = frequency_computer(inputs[index])
        return inputs


"""Convert each row of the file into the list of words 
  --------------------------------------------------------
  This function has objective of transforming the row of file into the list of words in each row
    """


def conv(self, stock_str):
    n = int(input('Enter the number of rows modify: '))

    for i in range(n):
        print(stock_str[i])
        liste = stock_str[i].split()

        #         st=','.join([item  for item in liste])
        stock_str[i] = liste

    return stock_str[:n]


"""Combination of two dictionaries to get one with updated values, here we take two rows that 
contains dictionaris and put them together to get one dictionary of updated keys and value
----------
This function will be useful to the time of finding frequency of each word in a whole document
"""


def dict_combine_2(self, dic1, dic2):
    return dict(sorted({k: dic1.get(k, 0) + dic2.get(k, 0) for k in set(dic1) | set(dic2)}.items()))


"""ENCODING DOCUMENT 
---------------------
  This function is going to use that function which combine two dictionaries and use it to get a frequency of each word in full document.
            """


def final_encoder(self):
    dict_store = self.row_to_dict()

    start = dict_store[0]

    for i in range(1, len(dict_store)):
        var = self.dict_combine_2(start, dict_store[i])
        start = var
    return start


"""Transform the  file
-----------------------------
This function is tasked to use a created functions, and produces the encoded file using the frequencies of words in a whole file.
"""


def transform(self):
    inputs = self.row_to_dict()
    temp = self.conv(self.data)

    ff = self.final_encoder(inputs[:5])

    final = []
    new_df = temp.copy()
    for idx, item in enumerate(temp):
        final = []
        for x in item:
            if x in ff.keys():
                final.append(ff[x])
        new_df[idx] = final

    return new_df
