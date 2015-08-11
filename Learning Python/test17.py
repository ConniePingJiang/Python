'''
4. Write a function that takes a character 
(i.e. a string of length 1) and returns True if it is 
a vowel, False otherwise.

Created on Aug 7, 2015

@author: conniejiang
'''
def tf(x):
    if(x=='a' or x=='o' or x=='u' or x=='i' or x=='e'):
        print(True)
    else:
        print(False)
tf('u')