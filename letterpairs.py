import string
def letter_pair():
    letters = string.ascii_lowercase
    
    for i in range(0, len(letters)):
        for j in range(0, len(letters)):           
            print(letters[i]+letters[j])
    
letter_pair()
#output:
# aa
# ab
# ...
# ba
# bb
# ...
# zz