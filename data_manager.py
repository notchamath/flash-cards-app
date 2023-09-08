import pandas
import random

FR = "French"
EN = "English"


class DataManager:
    def __init__(self):
        self.fr = FR
        self.en = EN
        self.word_list = []
        self.pull_data()
        self.word = None
        self.fr_word = None
        self.en_word = None
        self.get_word()

    # Pull data from csv using Pandas lib
    def pull_data(self):
        try:
            data = pandas.read_csv("./data/to_learn.csv")
        except FileNotFoundError:
            original_data = pandas.read_csv("./data/french_words.csv")
            self.word_list = original_data.to_dict(orient="records")
        else:
            self.word_list = data.to_dict(orient="records")

    # Get a random word from word_list
    def get_word(self):
        if len(self.word_list) > 0:
            self.word = random.choice(self.word_list)
            self.fr_word = self.word[FR]
            self.en_word = self.word[EN]
        else:
            self.completed()

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

    # End program if user gets all words correct
    def completed(self):
        end_title = "You got all the words right!"
        end_word = "Well Done!"
        self.fr = end_title
        self.en = end_title
        self.fr_word = end_word
        self.en_word = end_word
