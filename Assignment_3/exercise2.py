import random
import sys

user_choose = int(input ("Please Enter Length Of Array :"))
Array = [random.randrange(1, sys.maxsize, 1) for i in range(user_choose )]

print (Array)