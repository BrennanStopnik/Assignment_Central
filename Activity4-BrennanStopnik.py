#Declaring variables to store values
firstName = "Brennan"

lastName = "Stopnik"

favoriteColor = "green"

favoriteMeal = "my wifes meatloaf"

#F-string
sentence1 = f"My first name is {firstName}. My last name is {lastName}. My favorite color is {favoriteColor}. My favorite meal is {favoriteMeal}"

print(sentence1)

#Concatenate
sentence2 = "My first name is Brennan." + " " + "My last name is Stopnik." + " " + "My favorite color is green." + " " + "My favorite food is my wifes meatloaf."

print(sentence2)

#Argument by Postion
sentence3 = "My first name is {0}. My last name is {1}. My favorite color is {3}. My favorite meal is {2}".format("Brennan", "Stopnik", "my wifes meat loaf", "green")

print(sentence3)

#Argument by name
sentence4 = "My first name is {fName}. My last name is {lName}. My favorite color is {favColor}. My favorite meal is {favMeal}".format(fName = "Brennan", lName = "Stopnik", favColor = "green", favMeal = "my wifes meatloaf")

print(sentence4)