# This program prompts the user for 2 numbers and returns the first raised to the power of second
# and the log value of the first
import math

x = eval(input("Enter a number x: "))
y = eval(input("Enter a number y: "))
print("The result of {} raised to the power of {} is {}".format(x, y, math.pow(x, y)))
print("The result of log({}) is : {}".format(x, math.log2(x)))
