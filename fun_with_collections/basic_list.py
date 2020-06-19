def make_list():
    """return list of user input"""
    input_list = []
    for x in range(0, 3):
        input_list.append(get_input())
    return input_list


def get_input():
    """gets one user input then returns it"""
    x = input("Enter number for list: ")
    if x.isnumeric():
        return int(x)
    else:
        raise ValueError
