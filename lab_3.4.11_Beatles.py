""" step 1: create an empty list named beatles;
step 2: use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, and George Harrison;
step 3: use the for loop and the append() method to prompt the user to add the following members of the band to the list: Stu Sutcliffe, and Pete Best;
step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
step 5: use the insert() method to add Ringo Starr to the beginning of the list."""

# Code starts here 
beatles_list = []

#step 2
a = ("John Lennon", "Paul McCartney", "George Harrison")
beatles_list.append(a)

print( beatles_list, "beatles")

#step 3 
input_members = ["Stu Sutcliffe", "Pete Best"]
for i in input_members: 
    beatles_list.append(i)
    
print( beatles_list, "beatles")
print( beatles_list, "beatles")
print( beatles_list, "beatles")
print( beatles_list, "beatles")
