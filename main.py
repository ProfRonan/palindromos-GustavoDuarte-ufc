"""Main functions"""

def is_palindrome(string: str) -> bool:
    b = string.lower().replace(' ', '')

    if b[:] == b[::-1]:
        return True
    else:
        return False
