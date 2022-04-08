import time
import numpy as np


def run_time_find(word: str,data_struct: iter) ->time:
    """
    The function calculate run time of one search word in data structure
    :param word: word to search
    :param data_struct: Data structure for search in
    :return: The runtime of the search
    """
    start_time = time.time()
    word in data_struct
    return time.time() - start_time


def average_runtime(word: str,data_struct:iter)-> float:
    """
    The function calculate the average runtime of search word in data structure
    :param word: Word to search
    :param data_struct: Data structure for search in
    :return: The average run time
    """
    run_times = [run_time_find(word,data_struct) for _ in range(1000)]
    return np.mean(run_times)


def main():
    """
    The program compares the run times of a list search vs a set search
    """
    words_file = "C:\\Users\\nechama\\Notebooks\\week06\\resources\\words.txt"
    words_list=[]
    with open(words_file,'r') as file:
        words_list = file.read().split()
    words_set = set(words_list)
    word = "zwitterion"
    print("average runtime for list: " , average_runtime(word,words_list))
    print("average runtime for set: " , average_runtime(word,words_set))


if __name__ == "__main__":
    main()
    
