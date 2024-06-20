#Check If Number is even or odd (Fast Solution)

def EvenOdd(num):
    if num & 1 == 0:
        return str(num) + " is an even number"
    return str(num) + " is an odd number"

EvenOdd(1)