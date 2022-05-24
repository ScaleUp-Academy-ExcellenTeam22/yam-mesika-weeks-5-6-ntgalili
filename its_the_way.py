
import os


def files_start_with(path :str, prefix:str):
    """
    The function get a path of a directory and find the files in the directory that start with start
    :param path: the path of the directory
    :param prefix: the str that the file's names start with
    :return: list of files
    """
    list_of_files = os.listdir(path) # get the list of the files in the directory
    starts_files = [file for file in list_of_files if file.startswith(prefix)] # get the list of the files that start with start
    return starts_files


def main():

    path = input("Enter a path of directory: ")
    deep_file = files_start_with(path, 'deep') # find the files in the directory that start with 'deep'
    print(deep_file)


if __name__ == "__main__":
    main()
