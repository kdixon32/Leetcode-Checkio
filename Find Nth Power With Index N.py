# You are given a list with positive integers (int) and an integer (int) N. 
# You should find the N-th power of the element in the list with the index N. 
# If N is outside of the list, then return -1. 
# Don't forget that the first element has the index 0.

def index_power(array, n):
    try: return array[n] ** n
    except IndexError: return -1