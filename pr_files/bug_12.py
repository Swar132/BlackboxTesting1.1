def buggy_function_11():
    f = open('missing_file.txt', 'r')
    data = f.read()
    f.close()
    return data