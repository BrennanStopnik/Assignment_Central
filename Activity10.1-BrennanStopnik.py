'''
10.1 Activity

Write a function that will take in an intereger as a paremeter and will create a list of the size passed in as an argument, and will populate the list with a random number between 0-1023. You're going to use the "getrandbits()" method so think about how to arrive at that outcome.
'''

import random




def randList(num = 5):
    list = []                               #doing this is teh zero of lists. making sure you initailize the list
        
    for i in range(num):
        randNum = random.getrandbits(10)    #generate a Num between 0-1023 because it's 10 bits
        list.append(randNum)

    print(list)
    return list

randList(10)



# 10.2 Activity:

'''
Pronblem: generate a random number but don't use bits. use a decimal number.

Simliar to previous, generate a random number and 


randNum = random.randrange(0,10)
print(randNum)
'''

def randList2(num = 5):
    list2 = []                               
        
    for i in range(num):
        randNum = random.randrange(20, 40)    
        list2.append(randNum)

    print(list2)
    return list2

randList2(20)

