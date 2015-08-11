'''
12. Define a procedure histogram() that takes a list of 
integers and prints a histogram to the screen. For 
example, histogram([4, 9, 7]) should print 
the following:
****
*********
*******

Created on Aug 10, 2015

@author: conniejiang
'''
def histogram(x, y, z):
    for i in range(0, x):
        print('*', end = ' ')
    print()
    for f in range(0, y):
        print('*', end = ' ')
    print()
    for m in range(0, z):
        print('*', end = ' ')
histogram(1, 2, 3)