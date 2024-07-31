print("This is my factorial program")
def fact(num):
    if num == 1 or num == 0:
        return num
    else:
        return num * fact(num-1)


num = int(input("Enter Number"))
factorial = fact(num)
print(f'factorial of {num} is {factorial}')