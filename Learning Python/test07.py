'''
Created on Aug 6, 2015

@author: conniejiang
'''
def parrot(voltage, state='a stiff', action='voom'):
    print("__This parrot wouldn't ", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")
    
d={"voltage": "four million", "state": "bleedin' demised", "action":"VOOM"}
print(parrot(**d))