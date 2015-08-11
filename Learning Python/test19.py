'''
7. Define a function reverse() that computes the reversal 
of a string. For example, reverse("I am testing") should
return the string "gnitset ma I".

Created on Aug 9, 2015

@author: conniejiang
'''
def reverse(x):
    y = ""
    for i in range(0, len(x)):
        y = y + x[len(x)-1-i]
    return(y)
    
z=reverse('ConnieJiang')
print(z)