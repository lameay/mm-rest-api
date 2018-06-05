from collections import Counter


def get_file_word_count(file, delimiter=' '):

    contents = None

    file = open(file, 'r')
    if file.mode == 'r':
        contents = file.read()

    word_count = contents.split(delimiter)
    return word_count


def get_file_word_occurrences(words):
    return Counter(words)