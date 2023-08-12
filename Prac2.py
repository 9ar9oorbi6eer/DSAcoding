# activity number 1
#this is the menu
input("Press enter to display the menu")
print("1.Factorial iterative")
print("2.Factorial recursive")
print("3.Fibonacci recursive")
print("4.Fibonacci iterative")
print("5.Greatest common denominator recursion")
print("6.Number conversions")
user_input = int(input("please enter the number you want:"))

if user_input == 1:
# factorial iterative
    def calcNFactorial(n): 
        nFactorial = 1
        for ii in range(n, 1, -1):
            nFactorial = nFactorial * ii
        return nFactorial
    n = int(input("please enter a number:"))
    # not sure if they want the user to enter the input or it already being initalised.
    print(calcNFactorial(n))
    # n = 1558

elif user_input == 2:
# # factorial recursive 
    def calcNFactorialRecursive(n):
        if (n == 0):
            return 1
        else:
            return n * calcNFactorialRecursive(n-1)
    n = int(input("please enter a number:"))

    result = calcNFactorialRecursive(n)
    print(result)
    # the highest i can go is 998, n = 998

elif user_input == 3:
    # fibonacci recursive
    def fibRecursive(n):
        fibVal = 0

        if(n == 0):
            fibVal = 0
        elif(n == 1):
            fibVal = 1
        else:
            fibVal = fibRecursive(n-1) + fibRecursive(n-2)
        return(fibVal)
    n = int(input("please enter any number you want:"))
    result = fibRecursive(n)
    print(result)

elif user_input == 4:
# iterative fibonacci
    def fibIterative(n):
        fibVal = 0
        currVal = 1
        lastVal = 0

        if(n == 0):
            fibVal = 0
        elif(n == 1):
            fibVal = 1
        else:
            for ii in range(2,n+1):
                fibVal = currVal + lastVal
                lastVal = currVal
                currVal = fibVal
        return fibVal
    n = int(input("please enter a number:"))
    result = fibIterative(n)
    print(result)

# greatest common denominator
elif user_input == 5:
    def gcd_recursive(a, b):
        if b == 0:
            return a
        else:
            return gcd_recursive(b, a % b)

    
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    gcd = gcd_recursive(num1, num2)
    print("GCD of", num1, "and", num2, "is", gcd)
# source = chatgpt openAI https://chat.openai.com/

# number conversions
elif user_input == 6:
    def decimal_to_binary(decimal_num):
        if decimal_num == 0:
            return '0'
        elif decimal_num == 1:
            return '1'
        else:
            return decimal_to_binary(decimal_num // 2) + str(decimal_num % 2)

    decimal_num = float(input("Enter a decimal number: "))
    binary_num = decimal_to_binary(decimal_num)
    print(f"The binary representation of {decimal_num} is {binary_num}")
    # source = chatgpt openAI(https://chat.openai.com/)

