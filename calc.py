#Creating functions and performing operations with these functions
def add(input_1, input_2):
    if input_1 < 0 or input_2 < 0:
        return "Error: Negative values are not allowed"
    return input_1 + input_2

def subtract(input_1, input_2):
    if input_1 < input_2:
        return "Error: The 2nd input must be smaller than the 1st input"
    return input_1 - input_2

def multiply(input_1, input_2):
    if input_1 < 0 or input_2 < 0:
        return "Error: The inputs should be positive values"
    return input_1 * input_2

def divide(input_1, input_2):
    if input_2 != 0:
        return input_1 / input_2
    else:
        return "Error!"

# Getting user inputs
input_1 = int(input("Enter 1st input: "))
input_2 = int(input("Enter 2nd input: "))

# Calculate and print results
sum_result = add(input_1, input_2)
print("Sum of the entered integers:", sum_result)

subtract_result = subtract(input_1, input_2)
print("Difference of the entered integers:", subtract_result)

product_result = multiply(input_1, input_2)
print("Product of the entered integers:", product_result)

quotient_result = divide(input_1, input_2)
print("Quotient of the entered integers:", quotient_result)
