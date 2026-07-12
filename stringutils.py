def shout(text):
    return text.upper() + "!"


def is_palindrome(text):
    normalized = text.lower()
    return normalized == normalized[::-1]
