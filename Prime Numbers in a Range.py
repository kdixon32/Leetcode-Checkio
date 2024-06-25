# Provide a script that print every prime number in the range [10000;10050], on one line, separated by comas and spaces.

# The output (in the range [1;10]) should look like this:
# $ python3 solution.py
# 2, 3, 5, 7

def is_prime(n):
    if (n <= 1):
        return False
    for i in range(2, int(n**0.5)+1):  
        if (n % i) == 0:
            return False
    return True
    
def primes_in_range(n):
    if (n <= 1):
        return 0
    primes = []
    for i in range(10000, n):
       if (is_prime(i)):
            primes.append(i)
    print(', '.join(str(x) for x in primes))
    return

primes_in_range(10050)