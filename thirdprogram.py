#Name: Mary Clayton
#Date: 7/9/2022
#Purpose: Coding challenge (with random choices)

#INPUT
#import random number
import random
#declare num1, num2, total
num1 = random.randrange(0, 100000)
num2 = random.randrange(0, 100000)
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
print("Your first number is", num1, "and your second number is", num2)