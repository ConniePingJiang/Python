'''
Created on Aug 6, 2015

@author: conniejiang
'''
def add(num1, num2):
    return num1+num2

def sub(num1, num2):
    return num1-num2

def mul(num1, num2):
    return num1*num2

def div(num1, num2):
    return num1/num2


def main():
    operation = input("What do you want to do(+,-,*,/): ")
    if(operation!='+' and operation!='-' and operation!='*' and operation!='/'):
        #invalid Operation
        print("you must enter a valid operation")
    else:
        var1=int(input("Enter num1: "))
        var2=int(input("Enter num2: "))
        if(operation=='+'):
            print(add(var1, var2))
        elif(operation=='-'):
            print(sub(var1, var2))
        elif(operation=='*'):
            print(mul(var1, var2))
        else:
            print(div(var1, var2))
            
            
main()