def multiply(num1, num2):
    result = 0
    for i in range(num2):
        result += num1
    return result

def power(num, exponent):
    result = 1
    for i in range(exponent):
        result = multiply(result, num)
    return result

def square(num):
    return power(num, 2)
# test 
    num1 = 6
    num2 = 7
    exponent = 4

    print(f"{num1} * {num2} = {multiply(num1, num2)}")
    print(f"{num1}^{exponent} = {power(num1, exponent)}")
    print(f"{num1}^2 = {square(num1)}")
