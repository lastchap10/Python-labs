"""The continue statement is used to skip the current block and move ahead to the next iteration, without executing the statements inside the loop.

It can be used with both the while and for loops.

Your task here is very special: you must design a vowel eater! Write a program that uses:

a for loop;
the concept of conditional execution (if-elif-else)
the continue statement.
Your program must:

ask the user to enter a word;
use user_word = user_word.upper() to convert the word entered by the user to upper case; we'll talk about string methods and the upper() method very soon – don't worry;
use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
print the uneaten letters to the screen, each one of them on a separate line.
Test your program with the data we've provided for you."""

#code starts here

# Prompt the user to enter a word
user_word = input("Input your name: ") # creating a variable for user's name 

# and assign it to the user_word variable.


user_word = user_word.upper() # didn't work 

for letter in user_word: 
    # Complete the body of the for loop.
    if letter == "A": # I used lower case initially and didn't skip the letter because the word was converted to uppercase.I did change the letter a to uppercase
        continue # skips the current block and continues to the next iteration 

    elif letter == "E":
        continue

    elif letter == "I":
        continue

    elif letter == "O":
        continue

    elif letter == "U":
        continue

   # print(letter.upper()) I tried this because the output was in lower case from the mistake above. 
    print(letter) # Printing the letter from the 


