import os

from api.util.file_utils import *

def test_get_word_count():
    file = os.path.join("resource", "textfile.txt")

    print get_file_word_count(file)
    assert False


def test_get_word_occurrences():
    words = ['hee', 'hee', 'tee', 'bleh']

    print get_file_word_occurrences(words)
    assert False