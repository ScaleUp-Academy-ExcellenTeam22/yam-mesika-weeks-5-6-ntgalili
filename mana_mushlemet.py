

def is_complete(num_pieces: int) -> bool:
    """
    The function get a number and check if it complete meal
    :param num_pieces: number of pieces in the meal
    :return: true if the meal is complete and false if not
    """
    divisions = [div for div in range(1, num_pieces) if num_pieces % div == 0]  # Finding the possible divisions
    return num_pieces == sum(divisions)  # check if the number == the sum of it's possible divisions


def complete_meals() -> int:
    """
    The function returns the complete numbers
    :return:
    """
    meal = 6
    while True:  # go over the numbers
        if is_complete(meal):  # return the meal if it complete
            yield meal
        meal += 1


def main():
    """
    The program prints the complete numbers
    """
    for complete_meal in complete_meals():  # go over the complete numbers and print them
        print(complete_meal)


if __name__ == "__main__":
    main()
