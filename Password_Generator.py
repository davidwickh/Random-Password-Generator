import string, random
from random import randrange
import pandas as pd

alphabet = string.ascii_letters


#Initialising the password variable and count variable
password = ''
count = 1


#Asking what the user wants for password length and how many numbers they want
length = int(input('How long do you want your password to be? [6-25]? '))
numbers = int(input('How many numbers would like you in your password? '))



#Creating a set of 0's of length the same as the user specified length of password.
#This set is used to represent the passwords in binary where 0 equates to a letter..
#generated, and 1 eqauates to a number generated.
numpositions = [0] * length


#For loop that runs the same number of times as the user specifies the number of number chars they want in their password.
for n in range(numbers):
    #Creating var x which is a random position in the range of the password length
    x = randrange(length)

    #Checking that the random possition has not be selected in previous itterations
    while sum(numpositions) == count - 1:
        x = randrange(length)
        numpositions[x] = 1  
    
    else:
        numpositions[x] = 1
    count = count + 1
    
    
for z in range(length):

    if numpositions[z] == 0:
        password += random.choice(alphabet)
    
    if numpositions[z] == 1:
        password += str(randrange(10))
print('Your password:', password)

