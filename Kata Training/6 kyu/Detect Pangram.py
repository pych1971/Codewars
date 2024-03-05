from string import ascii_lowercase


def is_pangram(s):
    for i in ascii_lowercase:
        if i not in (s.lower()):
            return False
    return True
