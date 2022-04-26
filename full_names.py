import string


def full_names(first_names: list, last_names: list, min_length=float('-inf')) -> list:
    """
    The function create list of full names that are  longer than min_length
    :param first_names: list of first names
    :param last_names: list of last names
    :param min_length: min length of the full name
    :return: list of full names
    """
    return [(first_name + ' ' + last_name).title() for first_name in first_names for last_name in last_names
            if len(first_name + ' ' + last_name) > min_length]
