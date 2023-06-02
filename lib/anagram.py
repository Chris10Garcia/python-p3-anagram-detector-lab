
class Anagram:
    def __init__(self, word):
        self.word = word
        self.word_set = set(word)
    
    def match(self, words):

        # test if the length of the word is the same length as the word within the list
        # if it is, store it as a dictionary with the key the word and the value as a set of the word
        # { word : "w", "o", "r", "d"} 
        self.words_set = {word : set(word) for word in words if len(word) == len(self.word)}

        # test if the set of the word is the same as the word within the set
        # if it is, store the key (which is the word in it's original form) into a list
        results = [key for key,value in self.words_set.items() if value == self.word_set]
        
        return results
    

    # def 

    # ana_word = "enlist"
    # ana_word_set = set(ana_word)

    #d = {k:v for k, v in iterable}

    # words_set = [{word : set(word)} for word in words if len(word) == len(ana_word)]
    
    # words_set = {word : set(word) for word in words if len(word) == len(ana_word)}
    # results = [key for key, value in words() if value & ana_word]

    # results = [key for key,value in words_set.items() if value == ana_word_set]
    # print(results)
    # # print(words_set)