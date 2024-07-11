"""
#1) - create a variable called numOne and assign it with a float of 2

from operator import truediv


numOne = 2.0

#2) Create another varaible called numTwo and assign it with a float of 5

numTwo = 5.0

#3) create a third variable called numSum which captures the sum of numOne and numTwo

numSum = numOne + numTwo

#4) take an input from the user called numUser

numUser = int(input( "Enter:" ))

#5)a create a variable called highNumber with the value assigned to 10

highNumber = 10

#5b perform a decision within the code which will output "High Number" 
#if the product of numUser and numSum is greater than highNumber
#and "Low Number" if smaller than 10 
lowNumber = 5

product_num = numUser * numSum

print(product_num)

if product_num > highNumber:
    if lowNumber < 10:
        print("pass")
else: 
    print ("False")


#6) using a for loop create a list called firstList with the numbers 1-20 stored in it

list = []
 
for x in range (1, 21):
    list.append(x)
    print(list)

#7) create a second list called secondList which stores the value of the corresponding 
#index in the first list multiplied by 2. e.g. [2,4,6,8....]
    
second_list = []
for numbers in list:
    result = numbers * 2 
    second_list.append(result)
    print(second_list)

#8) create a third list called boolList which stores whether each element in secondList
#is higher than highNumber (True) or lower (False)
boolist = []
for s_num in range(len(second_list)):
    if s_num > highNumber:
        result_higher = "true"
        boolist.append(result_higher)
    else: 
        result_lower = "false"
        boolist.append(result_lower)
print(boolist)

"""
#Question 9 will be once we have completed Mod 41 and Mod 42 review Tuesday


#9a) create a func called numPrint that outputs a list of numbers between a starting 
#number and a finish number. The function should have two parameters startNumber and endNumber
#

#def numPrint(startNumber, endNumber=10):
 #   return list(range(startNumber, endNumber + 1))

#print(numPrint(9))
      
#9b) once you have done 9a, make a change so that if the user doesnt input an end number 
#it automatically uses 10


#10)create a function which takes in a list of numbers as an argument. It then returns the number
#of odd numbers within the list. For example [3,4,5] should return 2

"""
my_list = [1,2,3,4, 5, 6, 7,8]
odd_list = []

def my_func(): 
    for i in range(len(my_list)):
        if i % 2 != 0:
            odd_list.append(i)  
           
my_func()
print(odd_list)
"""
#11) create a tuple which stores the following values 3,4,6,5,3,5,7,8,5

goals = {3,4,6,5,3,5,7,8,5}

#print(tup)

#12) The values shown in question 10 refer to the number of goals scored by the following players 
#Rooney, Vardy, Heskey, Owen, Grielish, Sterling, Pele, Maradona, Walker
#Create a second tuple which stores these players
players = {"Rooney", "Vardy", "Heskey", "Owen", "Grielish", "Sterling", "Pele", "Maradona", "Walker"}

#print(players_tup)

#13)) using the above tuples, link them via a dictionary.

my_dict = {player: goal for player, goal in zip(players, goals)}
print(my_dict)
#for example, Rooney:3, Vardy:4 etc. You should use your two tuples to construct the 
#dictionary

"""

Solution

Let's go through each step of the provided assessment and write the corresponding Python code.
Steps 1 to 3:
	1. Create a variable called numOne and assign it with a float of 2.
	2. Create another variable called numTwo and assign it with a float of 5.
	3. Create a third variable called numSum which captures the sum of numOne and numTwo.
python
Copy code
numOne = 2.0
numTwo = 5.0
numSum = numOne + numTwo
Step 4:
	1. Take an input from the user called numUser.
python
Copy code
numUser = float(input("Enter a number: "))
Steps 5a and 5b:
5a. Create a variable called highNumber with the value assigned to 10. 5b. Perform a decision within the code which will output "High Number" if the product of numUser and numSum is greater than highNumber and "Low Number" if smaller than 10.
python
Copy code
highNumber = 10
if numUser * numSum > highNumber:
    print("High Number")
else:
    print("Low Number")
Step 6:
	1. Using a for loop create a list called firstList with the numbers 1-20 stored in it.
python
Copy code
firstList = [i for i in range(1, 21)]
Step 7:
	1. Create a second list called secondList which stores the value of the corresponding index in the first list multiplied by 2.
python
Copy code
secondList = [i * 2 for i in firstList]
Step 8:
	1. Create a third list called boolList which stores whether each element in secondList is higher than highNumber (True) or lower (False).
python
Copy code
boolList = [i > highNumber for i in secondList]
Step 9:
9a. Create a function called numPrint that outputs a list of numbers between a starting number and a finishing number. The function should have two parameters startNumber and endNumber.
9b. Once you have done 9a, make a change so that if the user doesn't input an end number it automatically uses 10.
python
Copy code
def numPrint(startNumber, endNumber=10):
    return list(range(startNumber, endNumber + 1))
# Example usage:
print(numPrint(1))       # Outputs numbers from 1 to 10
print(numPrint(1, 15))   # Outputs numbers from 1 to 15
Step 10:
	1. Create a function which takes in a list of numbers as an argument. It then returns the number of odd numbers within the list.
python
Copy code
def count_odd_numbers(numbers):
    return len([num for num in numbers if num % 2 != 0])
# Example usage:
print(count_odd_numbers([3, 4, 5]))  # Outputs 2
Step 11:
	1. Create a tuple which stores the following values: 3, 4, 6, 5, 3, 5, 7, 8, 5.
python
Copy code
goals = (3, 4, 6, 5, 3, 5, 7, 8, 5)
Step 12:
	1. The values shown in question 11 refer to the number of goals scored by the following players: Rooney, Vardy, Heskey, Owen, Grealish, Sterling, Pele, Maradona, Walker. Create a second tuple which stores these players.
python
Copy code
players = ("Rooney", "Vardy", "Heskey", "Owen", "Grealish", "Sterling", "Pele", "Maradona", "Walker")
Step 13:
	1. Using the above tuples, link them via a dictionary. For example, Rooney:3, Vardy:4 etc. You should use your two tuples to construct the dictionary.
python
Copy code
goals_dict = dict(zip(players, goals))
# Example usage:
print(goals_dict)
# Outputs:
# {'Rooney': 3, 'Vardy': 4, 'Heskey': 6, 'Owen': 5, 'Grealish': 3, 'Sterling': 5, 'Pele': 7, 'Maradona': 8, 'Walker': 5}
This completes the assessment. Each step is clearly defined and implemented as requested.

"""