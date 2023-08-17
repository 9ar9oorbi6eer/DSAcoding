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
    checking_input = True
    while checking_input:
        try: 
            n = int(input("please enter a number:"))
            result = (calcNFactorial(n))
            print("the factorial of", n, "is", result)
            checking_input = False
        except ValueError:
            print("Invalid input, please enter a valid number: ") 
        # n = 1558

elif user_input == 2:
# # factorial recursive 
    def calcNFactorialRecursive(n):
        if (n == 0):
            return 1
        else:
            return n * calcNFactorialRecursive(n-1)
    checking_input2 = True
    while checking_input2:
        try:
            n = int(input("please enter a number:"))
            result = calcNFactorialRecursive(n)
            print(result)
            checking_input2 = False
        except ValueError:
            print("Invalid input, please try again: ")
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
    checking_input_3 = True
    while checking_input_3:
        try:
            n = int(input("please enter any number you want:"))
            result = fibRecursive(n)
            print(result)
            checking_input_3 = False
        except ValueError:
            print("Invalid input, please try again: ")

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
    checking_input_4 = True
    while checking_input_4:
        try:
            n = int(input("please enter a number:"))
            result = fibIterative(n)
            print(result)
            checking_input_4 = False
        except ValueError:
            print("invalid input, please try again: ")

# greatest common denominator
elif user_input == 5:
    def gcd_recursive(a, b):
        if b == 0:
            return a
        else:
            return gcd_recursive(b, a % b)
    checking_input_5 = True
    while checking_input_5:
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            gcd = gcd_recursive(num1, num2)
            print("GCD of", num1, "and", num2, "is", gcd)
            checking_input_5 = False
        except ValueError:
            print("Invalid input, please try again: ")
# source = chatgpt openAI https://chat.openai.com/

# number conversions
elif user_input == 6:
    def convert_decimal_to_base(decimal_number, base):
        if decimal_number == 0:
            return ""
        else:
            remainder = decimal_number % base
            return convert_decimal_to_base(decimal_number // base, base) + get_char_from_digit(remainder)

    def get_char_from_digit(digit):
        if digit < 10:
            return chr(ord('0') + digit)
        else:
            return chr(ord('A') + digit - 10)

    decimal_number = int(input("Enter a decimal number: "))
    base = int(input("Enter a base number: "))
    result = convert_decimal_to_base(decimal_number, base)
    print(f"Decimal {decimal_number} in base {base} is: {result}")
                # source = chatgpt openAI(https://chat.openai.com/)
                



        