
import os


def file_start(path :str,start:str):
    """
    the function get a path of a directory and find the files in the directory that start with start
    :param path: the path of the directory
    :param start: the str that the file's names start with
    :return: list of files
    """
    list_of_files = os.listdir(path) # get the list of the files in the directory
    starts_files = [file for file in list_of_files if file.startswith(start)] # get the list of the files that start with start
    return starts_files


def main():
    path = input("Enter a path of directory: ")
    deep_file = file_start(path,'deep') # find the files in the directory that start with 'deep'
    print(deep_file)


if __name__ == "__main__":
    main()
