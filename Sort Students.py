#In this exercise we represent students as a pair of (mark, full_name), so a tuple of two elements.
#And in this exercise we represent students as lists of pairs, like:
#>>> students = [(85, "Susan"), (6, "Joshua"), (37, "Jeanette")]

#PART 1
#Write a function sort_by_mark that takes an argument from a list of students are returns a copy of it sorted by mark in descending order.
def sort_by_mark(my_class):
    my_class.sort(reverse = True)
    return my_class

#Part 2
#Write a function named sort_by_name that takes an argument from a list of students and returns a copy of it sorted by name in ascending order.
def sort_by_name(my_class):
    my_class.sort(key = lambda students: students[1])
    return my_class