"""

Program: average_score_practice.py

Author: Chase Van Blair

Last date modified: 6/19/20


The purpose of this program is to practice using kwargs and args

"""


def average_scores(*args, **kwargs):
    # Use *args for average calculation
    ret_val = []
    for key, value in kwargs.items():
        ret_val.append(value)
    total = 0
    for x in args:
        total += int(x)
    ave = total / len(args)
    return "name: %s gpa = %s course = %s with current average %s" % (ret_val[0], ret_val[1], ret_val[2], ave)


if __name__ == '__main__':
    print(average_scores(4, 3, 2, 4, name='Michelle', gpa='3.4', course_name='python'))
    print(average_scores(30, 2, 25, 15, name='chase', gpa='0.1', course_name='world'))
    print(average_scores(40, 16, 72, 32, name='ryan', gpa='4.0', course_name='c++'))
