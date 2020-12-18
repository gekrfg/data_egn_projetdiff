import unittest
from webapp import get_similar_tweets


class TestClassifier(unittest.TestCase):
    def test_a(self):
        self.assertRegex(
            get_similar_tweets('Make America Great Again!')[0],
            'Top 1 : We have to make America great again!'
        )

    def test_b(self):
        self.assertRegex(
            get_similar_tweets('Hello! I like you!')[0],
            'Top 1 : I like Michael Douglas!'
        )


if __name__ == '__main__':
    unittest.main()