#Name: Mary Clayton
#Date: 7/9/2022
#Purpose: Coding challenge

#INPUT
#declare num1, num2, total
num1 = int(input("Enter first number: "))
num2 = int(input ("Enter second number: "))
sum = num1 + num2
diff = num1 - num2
def numbers(num1, num2, sum, diff):
    #return true if the two given integer values are equal
    #or their sum or difference is 5
    if (num1 == num2) or (sum or diff == 5):
        return True
    else:
        return False
#OUTPUT
print(numbers(num1, num2, sum, diff))