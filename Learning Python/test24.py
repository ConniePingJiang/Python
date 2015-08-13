'''
9. Write a function is_member() that takes a value
(i.e. a number, string, etc) x and a list of values a, and
returns True if x is a member of a, False otherwise. (Note
that this is exactly what the in operator does, but for
the sake of the exercise you should pretend Python did not
have this operator.)
Created on Aug 12, 2015

@author: conniejiang
'''
def is_member(x, y):
    for i in range(0, len(y)):
        if(x == y[i]):
            return(True)
    return(False)
z = is_member(5,[  7, 9, 2, 6])
print(z)