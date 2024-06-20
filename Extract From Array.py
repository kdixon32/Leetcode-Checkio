#create a function that gets a tuple and returns a tuple with only 3 elements - the first, third and second element from the last for the given tuple.

def easy_unpack(elements: tuple) -> tuple:
    return (elements[0], elements[2], elements[-2])