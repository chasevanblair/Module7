import array as arr


def search_array(collection, term):
    i = 0
    for x in collection:
        if x == term:
            return i
        else:
            i += 1
    return -1

