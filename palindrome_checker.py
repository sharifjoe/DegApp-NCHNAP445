def is_palindrome(word):
    """To check if the word is a palindrome."""
    word = word.replace(" ","").lower()
    return word == word[::-1]