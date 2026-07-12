import unittest

from stringutils import shout, is_palindrome


class StringUtilsTest(unittest.TestCase):
    def test_shout(self):
        self.assertEqual(shout("hello"), "HELLO!")

    def test_is_palindrome_true(self):
        self.assertTrue(is_palindrome("level"))


if __name__ == "__main__":
    unittest.main()
