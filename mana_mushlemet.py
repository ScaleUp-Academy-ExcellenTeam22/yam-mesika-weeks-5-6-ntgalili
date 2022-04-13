

def is_perfect(pieces_in_meal: int) -> bool:
    """
    The function gets a number and checks if it is a complete meal
    :param pieces_in_meal: number of pieces in the meal
    :return:True if the meal is complete and False if not
    """
    divisors = [divisor for divisor in range(1, pieces_in_meal) if pieces_in_meal % divisor == 0]   # Finding the possible divisions
    return pieces_in_meal == sum(divisors)  # check if the number == the sum of it's possible divisions


def perfect_numbers() -> int:
    """
    The function returns the perfect numbers -  which are equal to the sum of the numbers that divide them
    :return: complete number
    """
    num_to_check = 6
    while True:  # go over the numbers
        if is_perfect(num_to_check):  # return the number if it perfect
            yield num_to_check
        num_to_check += 1


def main():
    """
    The program prints the perfect numbers
    """
    for complete_meal in perfect_numbers():  # go over the perfect numbers and print them
        print(complete_meal)


if __name__ == "__main__":
    main()
