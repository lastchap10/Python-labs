""" step 1: create an empty list named beatles;
step 2: use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, and George Harrison;
step 3: use the for loop and the append() method to prompt the user to add the following members of the band to the list: Stu Sutcliffe, and Pete Best;
step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
step 5: use the insert() method to add Ringo Starr to the beginning of the list."""

# Code starts here 
beatles_list = []

#step 2
# a = "John Lennon", "Paul McCartney", "George Harrison" didn't work 

beatles_list.append("John Lennon") # adding strings in the list 
beatles_list.append("Paul McCartney")
beatles_list.append("George Harrison")

print(beatles_list)

#step 3 
input_members = ["Stu Sutcliffe", "Pete Best"] # assigning members in a list 

for i in input_members:  # using for loop to add members
    beatles_list.append(i) # using append i to add members 

print( beatles_list, "beatles")

#step 4
del beatles_list[3] # deleting members from the list using the index
del beatles_list[3]


print( beatles_list, "beatles")

beatles_list.insert(3, "Ringo Starr") # inserting new member in the position 3 
print( beatles_list, "beatles")

