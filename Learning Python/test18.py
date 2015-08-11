'''
5. Write a function translate() that will translate a text
into "rövarspråket" (Swedish for "robber's language"). 
That is, double every consonant and place an occurrence
of "o" in between. For example, translate("this is fun")
should return the string "tothohisos isos fofunon".
Created on Aug 9, 2015

@author: conniejiang
'''
def translate(x):
    y = ""
    for I in range(len(x)):
        if(x[I]==' ' or x[I].upper()=='A' or x[I].upper()=='E' or x[I].upper()=='I' or x[I].upper()=='O' or x[I].upper()=='U'):    
                y = y + x[I]
        else:
            y = y + x[I] + 'o' + x[I]
            
    return(y)


s = translate('hi charlie jiang')
t = translate('i miss Helen')
print(s)
print(t)
print(s+t)