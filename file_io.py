"""

Program: file_io.py

Author: Chase Van Blair

Last date modified: 6/20/20


The purpose of this program is to have user input name and test scores,
write those to a file then read file by line to print it to the console

"""
def write_to_file(tup):
    """
    writes the scores and name to one line on file
    :param tup: tuple with name as [0] and scores as [1]
    :return:
    """
    with open('testfile', 'a') as file:
        separator = ", "
        score_list = separator.join(tup[1])
        append_data = file.write(tup[0] + ": " + score_list + '\n')


def get_student_info(student_name):
    """
    this is where user inputs test scores for each student
    :param student_name: student's name
    :return:
    """
    x = 0
    scores = []
    while x != "quit":
        x = input("Enter test score for %s, or \"quit\" to stop: " % student_name)
        if x != "quit":
            scores.append(x)

    write_to_file([student_name, scores])


def read_from_file():
    """
    reads out and prints each line in the file
    :return:
    """
    with open('testfile', 'r') as file:
        lines = file.readlines()
        for x in lines:
            print(x.strip())


if __name__ == "__main__":
    get_student_info("jeff")
    get_student_info("bob")
    get_student_info("chris")
    get_student_info("anne")
    read_from_file()
