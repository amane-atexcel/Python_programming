#Week 1 python programming assignment
#Instruction Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).

#Ask for inputs
num1= float(input("Enter the first number: ")) #the code converts the user input into float data type
num2= float(input("Enter the second number: "))
operator= input("Enter operator(+, -, *, /): ")

#Performing calculation based on user inputs
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1/num2
    else:
        result = "Undefined (division by zero )"
else:
    result = "Invalid operator"

#Finally printing the result
print(f"{num1}{operator}{num2}={result}")