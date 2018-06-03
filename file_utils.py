def file_word_count(file, delimiter=' '):

    contents = None

    file = open(file, 'r')
    if file.mode == 'r':
        contents = file.read()
    return contents