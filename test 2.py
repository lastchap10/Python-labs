secret_word = int(22)

while True: # using while true function to create a loop and create a condition. 

    word = input("Input the word: ") # user required to input a number

    if word != secret_word: # finding if the number matches the secret number
        print("Haha! You're stuck in the loop") # Printing the message 

    else:
        print(f"{word}") # if condition not true, it repeats the function number again 
        print("Well done, muggle! You are free now.")

        #break # breaking the loop 