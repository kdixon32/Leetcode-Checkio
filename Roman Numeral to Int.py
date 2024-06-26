# Write a function named from_roman_numeral that return the value of a given roman numeral.

# Example
# >>> print(from_roman_numeral("V"))
# 5
# >>> print(from_roman_numeral("XX"))
# 20
# >>> print(from_roman_numeral("DCCC"))
# 800
# >>> print(from_roman_numeral("MMMM"))
# 4000
def from_roman_numeral(roman_numeral):
    inroman = {}
    
    inroman["M"] = 1000
    inroman["CM"] = 900
    inroman["D"] = 500
    inroman["CD"] = 400
    inroman["C"] = 100
    inroman["XC"] = 90
    inroman["L"] = 50
    inroman["XL"] = 40
    inroman["X"] = 10
    inroman["IX"] = 9
    inroman["V"] = 5
    inroman["IV"] = 4
    inroman["I"] = 1
   
    romansum = 0
    last = "I"
    arr = list(roman_numeral)
    for i in arr[::-1]: #BACKWARDS works better
        if inroman.get(i) < inroman.get(last):
            romansum -= int(inroman.get(i))
        
        else:
           romansum += inroman.get(i)
           last = i
           
    return romansum