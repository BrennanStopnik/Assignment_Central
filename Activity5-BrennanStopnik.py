#Create a Tuple with different data types

myTuple = ("Happiness", 100, True, "Spacetime Continuum", "James Reece", "hello")

print(myTuple) 

# Create a tuple with multiple values and print last item.

myTuple2 = (10, 20, 55, 143, 1212,)


print(myTuple2[-1])

#get the 4th from the front and 4th from the back

ftf = myTuple2[3]

ftb = myTuple2[-4]

print(ftf)
print(ftb)

print(myTuple2[2], myTuple[4])

#length of a tuple

myTuple4 = (1, 2, 3, 4, 5, 6, 7)

myTup = len(myTuple4)

print(myTup)