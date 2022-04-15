import random
import time
from typing import Callable


def timer(function_to_check: Callable, *params_for_function, **k_params_for_function) -> time:
    """
    THe function calculates the run time of function
    :param function_to_check: function to calculate it's time
    :param params_for_function: params for the function
    :param k_params_for_function: key params to the function
    :return: the run time of the function
    """
    start_time = time.time()
    function_to_check(*params_for_function,**k_params_for_function)  # apply the function
    return time.time() - start_time

