from core import most_frequent_words, remove_stop_words, most_freq
import unittest


class TestCore(unittest.TestCase):
    def setUp(self) -> None:
        self.word_dict = {"1": 'Hari Seldon Hari Seldon is a fictional character',
                          "2": 'Seldon develops psychohistory an algorithmic science',
                          "3": 'The significance of his discoveries lies behind his nickname Raven Seldon'}
        self.sentence = "Hari Seldon Hari Seldon is a fictional character. \
                         Seldon develops psychohistory an algorithmic science. The significance of his\
                         discoveries lies behind his nickname Raven Seldon"

    def test_most_frequent(self):
        op_list = [('Seldon', 4), ('Hari', 2), ('his', 2), ('is', 1), ('a', 1)]
        predicted_op = most_frequent_words(self.word_dict, 5)
        self.assertEqual(predicted_op, op_list)

    def test_remove_stop_words(self):
        self.assertEqual(' is ' in self.sentence, True)
        self.assertEqual(' a ' in self.sentence, True)
        filtered_sentence = remove_stop_words(self.sentence)
        self.assertEqual(' is ' in filtered_sentence, False)
        self.assertEqual(' a ' in filtered_sentence, False)

    def test_most_freq(self):
        d = most_freq(self.word_dict)
        print(d)
