import itertools


def interleave(*iterables: iter):
    """
    THe function get iterables and merge them alternately
    :param iterables: iterables objects to merge
    :return: the organs of the merged list
    """
    for organs in itertools.zip_longest(*iterables, fillvalue=None):  # Go over the iterables organs by locations
        for organ in organs:  # returns the organs
            yield organ
