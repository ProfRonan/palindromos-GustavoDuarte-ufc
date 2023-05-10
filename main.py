"""Main functions"""
import re

def is_palindrome(string: str) -> bool:
    b = string.lower()
    d = re.sub('[.,! s?@:;]', '', b)
    c = d[::-1]
    if d == c:
        return True
    else:
        return False
