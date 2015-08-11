'''
Created on Aug 6, 2015

@author: conniejiang
'''
def make_incrementor(n):
    return lambda x: x+n

f = make_incrementor(42)
print(f(1))