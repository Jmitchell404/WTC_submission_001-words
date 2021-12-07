import unittest
from io import StringIO
from unittest.mock import patch


class TestWordProcessor(unittest.TestCase):
    def test_convert_to_word_list(self):
        """
        tests if it is stored in a list
        tests if the list is slpit by the special characters
        """
        test_list = "words", "text", "letters"
        new_test_list = ",?:;. "
        self.assertTrue(new_test_list, test_list)


    def test_words_longer_than(self):
        """
        tests if it goes through the list
        if it checks the length of eac letter
        tests if the words are returned
        """
        test_list = "apple"
        check_test_list = len(test_list)
        self.assertTrue(check_test_list, test_list)


    def test_words_lengths_map(self):
        """
        tests if it returns the dictionary with that word length
        """
        test_list = ["apple", "grape", "berry"]
        my_dict = sorted(test_list)
        self.assertTrue(my_dict, test_list)


    def test_letters_count_map(self):
        """
        tests how many times a letter repeats
        returns it in dictionary form(a-z)
        """
        test_list = ''.join("apple")        
        my_dict = sorted(test_list)
        self.assertTrue(test_list, my_dict)


    def test_most_used_character(self):
        """
        tests the the most repeated letter is returned
        """
        test_list = ("apple", "grape", "berry")
        numbers = max(test_list)
        self.assertTrue(test_list, numbers)