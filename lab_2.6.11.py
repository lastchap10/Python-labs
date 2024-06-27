hour = int(input("Starting time (hours): ")) # user to input the starting hour, converts the input to an integer, and assigns it to the variable
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# find a total of all minutes
mins= mins+dura 

# find a number of hours hidden in minutes and update the hour

hour= hour+mins // 60 #Calculates how many whole hours are in the total minutes

# correct minutes to fall in the (0..59) range

mins = mins%60   #calculates the remainder when the total minutes are divided by 60

# correct hours to fall in the (0..23) range
hour = hour % 24 #calculates the remainder when the total hours are divided by 24. This ensures the hour value falls within the range 0 to 23
print(hour, ":", mins, sep='')