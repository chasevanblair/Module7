import array as arr


def search_array(collection, term):
    i = 0
    for x in collection:
        if x == term:
            return i
        else:
            i += 1
    return -1


def sort_array(collection):
    new_array = arr.array('i', [])
    init_len = len(collection)
    for x in range(0, init_len):
        lowest = collection[0]
        for y in range(0, len(collection)):
            if lowest > collection[y]:
                lowest = collection[y]
        new_array.append(lowest)
        collection.remove(lowest)

    return new_array
