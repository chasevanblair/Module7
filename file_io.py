def write_to_file(tup):
    with open('testfile', 'a') as file:
        append_data = file.write(tup + '\n')


def get_student_info(student_name):
    x = 0
    scores = []
    while x != "quit":
        x = input("Enter test score, or \"quit\" to stop")
        if x != "quit":
            scores.append(x)

    write_to_file(scores)


def read_from_file():
    with open('testfile', 'r') as file:
        lines = file.readlines()
        for x in lines:
            print(x.strip())


if __name__ == "__main__":
