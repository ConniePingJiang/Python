'''
18. A pangram is a sentence that contains all the letters 
of the English alphabet at least once, for example: 
The quick brown fox jumps over the lazy dog. Your task 
here is to write a function to check a sentence to see 
if it is a pangram or not.

Created on Aug 12, 2015

@author: conniejiang
'''
def pangram(x):
    y = x.lower()
    a = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(0, len(a)):
        if(a[i] not in y):
            return(False)
    return(True)
z = pangram('the quick brown fox jumps over the Lazy dog')
print(z)
             
            