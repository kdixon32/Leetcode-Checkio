# You are given list of integers (int). You should find the sum of the elements with even indexes (0th, 2nd, 4th...). Then multiply this summed number and the final element of the list together. Don't forget that the first element has an index of 0.
# For an empty list, the result will always be 0 (zero).

def checkio(array: list[int]) -> int: 
    try: return sum(array[::2]) * array[-1]
    except IndexError: return 0