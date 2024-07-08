"""Your task is to write and test a function which takes two arguments (a year and a month) and returns the number of days for the given year-month pair (while only February is sensitive to the year value, your function should be universal).

The initial part of the function is ready. Now, convince the function to return None if its arguments don't make sense.

Of course, you can (and should) use the previously written and tested function (LAB 4.3.1.6). It may be very helpful. We encourage you to use a list filled with the months' lengths. You can create it inside the function ‒ this trick will significantly shorten the code.

We've prepared a testing code. Expand it to include more test cases."""


def is_year_leap(year):
    #
    # Your code from the previous LAB.
    # Check if the year is a leap year
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def days_in_month(year, month):
    if year < 1582 or month < 1 or month > 12: # condition to ensure the month is valid 
     return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # list with number if days assigned in the list
    if month == 2 and is_year_leap(year): # condition to find if the year is leap year 
        res = 29 # if it is leap year the no of days is 29
        return res
    else: 
        return days[month - 1] # returns the coresponding days month -1 eg for march (3 -1)is index 2 which gives 31 days 

# test datas in 3 lists 
    
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30] 

for i in range(len(test_years)): # setting for loops to iterate all the test years 
    yr = test_years[i] # creating variables yr and months foe each indexes 
    mo = test_months[i]
    print(yr, mo, "->", end="") # printing the outputs 
    result = days_in_month(yr, mo) # outputs the total days for correponding yr and month resulted from the days in month 
    if result == test_results[i]: # comparing output result with the test results 
        print("OK")
    else:
        print("Failed")
