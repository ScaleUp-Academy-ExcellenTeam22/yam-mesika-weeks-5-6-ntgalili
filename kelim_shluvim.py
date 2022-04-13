import itertools


def interleave(*iterables: iter):
    """
    The function gets iterables and merges them alternately
    :param iterables: iterable objects to merge
    :return: the elements of the merged list
    """
    for elements in itertools.zip_longest(*iterables, fillvalue=None):  # Go over the iterables elements by locations
        for element in elements:  # returns the organs
            yield element
