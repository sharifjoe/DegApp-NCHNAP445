import unittest
from palindrome_checker import is_palindrome

class TestPalindromeChecker(unittest.TestCase):
    """Unit tests for is_palindrome function."""

    def test_empty_string(self):
        """Test that an empty string is a palindrome."""
        self.assertTrue(is_palindrome(""))

    def test_single_character(self):
        """Test that a single character is a palindrome."""
        self.assertTrue(is_palindrome("a"))

    def test_palindrome_word(self):
        """Test that a palindrome returns True."""
        self.assertTrue(is_palindrome("rotor"))

    def test_mixed_case_palindrome(self):
        """Test that a palindrome with mixed cases returns True."""
        self.assertTrue(is_palindrome("rOTor"))

    def test_palindrome_with_spaces(self):
        """Test that a palindrome phrase with spaces returns True."""
        self.assertTrue(is_palindrome("go deliver a dare vile dog"))

if __name__ == "__main__":
    unittest.main()