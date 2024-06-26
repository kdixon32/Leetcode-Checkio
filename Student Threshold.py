# Write a function telling appart accepted and refused students according to a threshold.

# The function should be called select_student and takes as arguments:

# A list where each element is a list of a student name, and his grade.
# A grade. The student grade must be superior or equal to the given grade to be accepted.
# Your function must return a dictionnary with two entries:

# Accepted which list the accepted students sorted by grades in the descending order.
# Refused which list the refused students sorted by grades in ascending order.
# Example
# In [1]: from solution import select_student

# In [2]: my_class = [['Kermit Wade', 27], ['Hattie Schleusner', 67], ['Ben Ball', 5], ['William Lee', 2]]

# In [3]: select_student(my_class, 20)
# Out[3]:
# {'Accepted': [['Hattie Schleusner', 67], ['Kermit Wade', 27]],
#  'Refused': [['William Lee', 2], ['Ben Ball', 5]]}

# In [4]: select_student(my_class, 50)
# Out[4]:
# {'Accepted': [['Hattie Schleusner', 67]],
#  'Refused': [['William Lee', 2], ['Ben Ball', 5], ['Kermit Wade', 27]]}

def select_student(students, threshold):
    Accepted = []
    Refused = []
    
    for i in students:
        if i[1] >= threshold:
            Accepted.append(i)
        else:
            Refused.append(i)
    return {
        'Accepted': sorted(Accepted, key=lambda student: student[1], reverse=True),
        'Refused': sorted(Refused, key=lambda student: student[1])
        }
        