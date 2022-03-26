import random
import datetime


def find_date_between(date1:datetime,date2:datetime):
    """
    the function find date between two dates
    :param date1: first date
    :param date2: second date
    :return: the new date
    """
    epoch1 = date1.timestamp()  # find the epoch of the dates
    epoch2 = date2.timestamp()
    rand_epoch = random.randint(epoch1, epoch2)  # find a new epoch between the 2 epochs
    return datetime.datetime.fromtimestamp(rand_epoch)  # find the new date


def is_monday(date:datetime):
    """
    check if the day of the date is monday
    :param date: date
    :return: is the day of the date == 2
    """
    return date.weekday() == 2


def main():
    strdate1 = input("Enter a date (YYYY-MM-DD)")  # gets 2 dates
    strdate2 = input("Enter a date (YYYY-MM-DD)")
    date1 = datetime.datetime.strptime(strdate1, '%Y-%m-%d')
    date2 = datetime.datetime.strptime(strdate2, '%Y-%m-%d')

    new_date=find_date_between(date1,date2)  # find the new date

    print(new_date.strftime('%Y-%m-%d'))
    if is_monday(new_date):
        print("I have no vinaigrette!")


if __name__ == "__main__":
    main()