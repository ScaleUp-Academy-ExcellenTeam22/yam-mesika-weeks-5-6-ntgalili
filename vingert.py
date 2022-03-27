import random
import datetime


def find_date_between(first_date:datetime,end_date:datetime):
    """
    the function find date between two dates
    :param first_date: first date
    :param end_date: second date
    :return: the new date
    """
    first_epoch = first_date.timestamp()  # find the epoch of the dates
    end_epoch2 = end_date.timestamp()
    rand_epoch = random.randint(first_epoch, end_epoch2)  # find a new epoch between the 2 epochs
    return datetime.datetime.fromtimestamp(rand_epoch)  # find the new date


def is_monday(date:datetime):
    """
    check if the day of the date is monday
    :param date: date
    :return: is the day of the date == 2
    """
    return date.weekday() == 2


def main():
    first_date_str = input("Enter a date (YYYY-MM-DD)")  # gets 2 dates
    end_date_str = input("Enter a date (YYYY-MM-DD)")
    first_date = datetime.datetime.strptime(first_date_str, '%Y-%m-%d')
    end_date = datetime.datetime.strptime(end_date_str, '%Y-%m-%d')

    new_date=find_date_between(first_date,end_date)  # find the new date

    print(new_date.strftime('%Y-%m-%d'))
    if is_monday(new_date):
        print("I have no vinaigrette!")


if __name__ == "__main__":
    main()