import datetime
import time

print("bounds are inclusive")

lowerBound=int(input("Lower Bound? "))
upperBound=int(input("Upper Bound? "))

mod = (upperBound-lowerBound)+1 #the range between the upper and lower bound.
microsecond=(datetime.datetime.now()).microsecond #microsecond value of the time
random = (1664525*microsecond + 1013904223)#randomises this value more
number = (random%mod)+lowerBound #generates random number by calculating a remainder

print(number)

