#Write a Program to check the greatest among 3 Numbers


# threeNums = 10 > 5 > 3

# print(threeNums)

a = 23
b = 25
c = 21

if(a > b and a > c):
    print("A is the greatest")
elif(b > a and b > c):
    print("B is the greatest")
else:
    print("C is the greatest")


#Write a Program to imitate a Traffic light. Think about the information you need to generate to make your program mimic the real world


greenLight = True
yellowLight = False
youreClose = True

if(greenLight):
    print("Go!")
elif(yellowLight):
    if(youreClose):
        print("Hit the gas!")
    else:
        print("Stomp on the brakes.")
else:
    print("Stop.")
