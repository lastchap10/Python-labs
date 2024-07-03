print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
secret_number = 777

while True: # using while true function to create a loop and create a condition. 

    number = int(input("Input the number: ")) # user required to input a number

    if number != secret_number: # finding if the number matches the secret number
        print("Haha! You're stuck in the loop") # Printing the message 

    else:
        print(f"{number}") # if condition not true, it repeats the function number again 
        print("Well done, muggle! You are free now.")

       # break # breaking the loop 





