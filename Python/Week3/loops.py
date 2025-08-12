##Conditional statement there are three types: if,  if else, elif
#Loop statements repeat a block of code, process of iteration while-indefinite loop, for definite loop
for n in range(1, 6):
    print(f"The number is: {n}")

#Nested loops

for i in range(1,4):
    for j in range(1,4):
        print(f"The outer loop: {i} The inner loop:{j}")

nmb = [x**2 for x in range(5)]
print(nmb)

#This code will do calculation to the power of 3 minus 1 in the range from 2 to 9
#The difference from the other for, it will assign to variable iteratively
hui = [x**3-1 for x in range(2,9)]
print(hui)

#while loop indefinite looping which will iterate until the condition is false
count = 1
while count <=5:
    print(f"The number is: {count}")
    count+=1

# the position of the increament statement matters if it is inside the colon in the below 
count = 1
while count <=5:
    count+=1
    print(f"The number is: {count}")

#List comprehension writing clear and simple list
hjy = [f**2-4 for f in range(10)]
print(hjy)

#Declaring function in Python
def add(a, b):
    return a+b
resul = add(3456,786532)
print(resul)
