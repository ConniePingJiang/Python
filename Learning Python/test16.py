'''
2.Define a function max_of_three() that takes three 
numbers as arguments and returns the largest of them.

Created on Aug 7, 2015
@author: conniejiang
'''
def max_of_three(num1, num2, num3):
    if(num1>num2>num3):
        print(num1)
    elif(num1>num3>num2):
        print(num1)
    elif(num2>num3>num1):
        print(num2)
    elif(num2>num1>num3):
        print(num2)
    elif(num3>num2>num1):
        print(num3)
    elif(num3>num1>num2):
        print(num3)
max_of_three(5, 3, 4)