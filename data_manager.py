import pandas
import random

FR = "French"
EN = "English"


class DataManager:
    def __init__(self):
        self.fr = FR
        self.en = EN
        self.word_list = []
        self.word = None
        self.pull_data()
        self.fr_word = None
        self.en_word = None
        self.get_word()

    # Pull data from csv using Pandas lib
    def pull_data(self):
        data = pandas.read_csv("./data/french_words.csv")
        self.word_list = data.to_dict(orient="records")

    # Get a random word from word_list
    def get_word(self):
        if len(self.word_list) > 0:
            self.word = random.choice(self.word_list)
            self.fr_word = self.word[FR]
            self.en_word = self.word[EN]

    # If user got the word correctly remove word from word_list
    def got_correct(self):
        if len(self.word_list) > 0:
            self.word_list.remove(self.word)
            data = pandas.DataFrame(self.word_list)
            data.to_csv("./data/to_learn.csv")
            self.get_word()

    # If user got the word wrong, get a new word
    def got_wrong(self):
        self.get_word()
