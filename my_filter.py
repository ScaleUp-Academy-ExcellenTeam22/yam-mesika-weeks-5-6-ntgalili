from typing import Callable


def my_filter(function_to_apply: Callable ,iterable: iter) -> list:
    """
    The function applies the function it received on the iterable and filters the True results
    :param function_to_apply: function to apply on the iterable
    :param iterable: Iterable used as parameters for the function
    :return: List of returned results whose value is true
    """
    return [function_to_apply(item) for item in iterable if function_to_apply(item)]

