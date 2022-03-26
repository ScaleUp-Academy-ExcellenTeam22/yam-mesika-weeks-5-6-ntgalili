
def join(*lists,sep='-'):
    """
    The function receives lists and joins them into one list
    :param lists:lists to join
    :param sep: Character to be placed between lists
    :return: The list that created
    """
    if len(lists) == 0:
        return None
    joined_list=[]
    [joined_list.extend(lst+[sep]) for lst in lists]  # join all the lists
    return joined_list[:-1]


# print(join([1,2,3],[2,3,4],['a','a',4]))
