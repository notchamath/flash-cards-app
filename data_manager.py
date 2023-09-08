import pandas
import random

FR = "French"
EN = "English"


class DataManager:
    def __init__(self):
        self.fr = FR
        self.en = EN
        self.data = None
        self.word_list = []
        self.pull_data()
        self.correct_list = []
        self.fr_word = None
        self.en_word = None
        self.get_word()

    def pull_data(self):
        data = pandas.read_csv("./data/french_words.csv")
        self.word_list = data.to_dict(orient="records")

    def get_word(self):
        word = random.choice(self.word_list)
        self.fr_word = word[FR]
        self.en_word = word[EN]

        print(self.correct_list)

    def got_correct(self):
        self.correct_list.append(self.fr_word)
        self.get_word()

    def got_wrong(self):
        self.get_word()
