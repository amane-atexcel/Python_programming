#Week assignment prepared by Amanuel Efrem
#Submission date August 11, 2025 as per given in the LMS

#Create empty list 
my_list = []

#Append elements to the list
append_l = [10,20,30,40]
for value in append_l:
    my_list.append(value)

#Insert the value 15 at the second position in the last
my_list.insert(1,15)

#Extend my_list with [50, 60, 70]
extend_list = [50, 60, 70]
my_list.extend(extend_list)

#Remove the last element from my_list
my_list.pop()

#Sort my_list in ascending order
my_list.sort()

#find and print the index of the value 30 in my_list
print(my_list.index(30))