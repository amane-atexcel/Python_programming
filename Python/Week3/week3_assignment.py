#Week 3 Python assignment on building calculate discount function

#Creating function first

def calculate_discount(price, discount_percent):
    '''The function will use two arguments, price and and discount percent '''
    if discount_percent >=20:
        discount = price * (discount_percent/100)
        final_price = price-discount
        return final_price
    else:
        return price  #If the condition does not meet i.e no discount will be applied

#The following lines of code prompts user to enter number, if the value is not numeric it will show error message.2

try:
    price= float(input("Enter the original price of an item: "))
    discount_percent= float(input("Enter the discount percentage: "))
    final_discount = calculate_discount(price, discount_percent)

    if discount_percent >= 20:
        print(f"Final price after {discount_percent:.0f}% discount: ${final_discount:.2f}")
    else:
        print(f"No discount applied. Final price will be: ${final_discount:.2f}")
except ValueError:
    print("Invalid input! Please enter numeric value, and rerun the program!")
