import unittest

from stringutils import shout, is_palindrome


class StringUtilsTest(unittest.TestCase):
    def test_shout(self):
        self.assertEqual(shout("hello"), "HELLO!")

    def test_is_palindrome_true(self):
        self.assertTrue(is_palindrome("level"))

    def test_is_palindrome_false(self):
        self.assertFalse(is_palindrome("hello"))

    def test_is_palindrome_empty_string(self):
        self.assertTrue(is_palindrome(""))


if __name__ == "__main__":
    unittest.main()
