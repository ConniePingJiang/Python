'''
Created on Aug 7, 2015

@author: conniejiang
'''
answer = input("Hello How are you doing today? Are you doing well or not well?: ")
if(answer != 'well' and answer != 'not well'):
    print("Please answer with well or not well the next time you run this")
else:
    if(answer == 'well'):
        print("Awesome! I hope it stays that way")
    else:
        print("Hopefully your day gets better")