# List comprehension = A concise way to create a list in Python
#                     Compact and easier to read than traditional loops

my_list=[] #This is question 1
my_list.append(10) # This is question 2
my_list.insert(1, 15) # insert the value 15 at the second position in the list, this is question 3
my_list.append(20)
my_list.append(30)
my_list.append(40)
# extend the list [50,60,70] this is question 4
my_list.append(50)
my_list.append(60)
my_list.append(70)

my_list = [10,15,20,30,40,50,60,70]

# remove the last element from the list. This is question 5
my_list.pop()
print(my_list) # This is question 6

# find and print the index of the value 30. This is question 7
my_list = [30]
print(my_list.index[30])