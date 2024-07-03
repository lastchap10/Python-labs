hour = int(input("Starting time (hours): ")) # user to input the starting time in hour, converts the input to an integer, 
# and assigns it to the hour variable
mins = int(input("Starting time (minutes): ")) # same as above for mins 
dura = int(input("Event duration (minutes): ")) # same as above for duration

# find a total of all minutes
mins= mins+dura # finding the total minutes by adding mins (start time) and the duration (in minutes) which gives you total minutes.

# find a number of hours hidden in minutes and update the hour

hour= hour+mins // 60 #calculating total hrs by adding hour variable (start time) and the whole hr
# (total mins but converting duration mins into a whole hr using floor division)'''

# correct minutes to fall in the (0..59) range

mins = mins%60   # calculating total minute which is remainder of the minute, from the whole hr, using modulo operator.

# correct hours to fall in the (0..23) range
hour = hour % 24 #calculates the end time hour modulo by 24. This ensures the hour value falls within the range 0 to 23
print(hour, ":", mins, sep='')