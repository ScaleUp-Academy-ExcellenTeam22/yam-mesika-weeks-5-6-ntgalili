import re
import string


def count_word(text: str)-> dict:
    """
    The function creates a dictionary of words and their lengths from the given text.
    :param text: text to analise
    :return: a dict of words and their len
    """
    words = {word.lower() for word in re.split('(\W+?)',text) if word not in string.punctuation +'\n'+' '}
    return {word:len(word) for word in words}

