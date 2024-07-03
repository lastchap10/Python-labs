secret_number = 7  # The secret number picked by the magician

while True:
    user_input = int(input("Enter an integer number: "))
    if user_input == secret_number:
        print(f"{user_input}")
        print("Well done, muggle! You are free now.")
        break
    else:
        print("Ha ha! You're stuck in my loop!")