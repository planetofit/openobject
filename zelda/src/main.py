#simple 'get' api to respond to a blinking variable holding a math operator
#math operator is variablized in a var of open object type
#basically get and set in one go but using hyperthreading
#math of 3n........
#-------- output devops recipe 'terraform deploy'
#some work from developers required to 
# open source project: def ob(3680) ----> run this function in 2 times parallel to each other issued by two systems which issues times from a same source such as utc.poit.network or time.windows.net
#-----> api call comes in, number of required variables determined, and circulate them using uncertainty principle of 3x+1 (start is nounce value and stop is max of the int of the numbered(vars) / depend on prcoess defined (repos)/triggers -> start time)
 
#import os

#3x+1 Conjucture
"""
i = 1
all_sets = []
maxNum = 0
results = []
while i < 7:
    num = i
    while num == 1:
        if (num % 2) == 0:
            if num == 1:
                    break
            num = num / 2
            results.append(num)
        else:
            if num == 1:
                    break
            num = num * 3 + 1
            results.append(num)
    i += 1
#print(results)
#maxNum = max(results)
print(results)
"""
import sys

file1=open('./file1', 'r').read()
file2="./file2"

x=0
y=0
maxOp = []

def evenFunc(x):
    y = int(x/2)
    return y

def oddFunc(x):
    y = int(3*x+1)
    return y


if len(sys.argv) == 0:
    x=6
    with open(file1, "rb") as f:
        while (byte := f.read(1)):
            x=x*f
else:
    for item in sys.argv:
        if item == sys.argv[0]:
            continue
        else:
            x=int(item)
            #x=int(sys.argv[1])
            with open(file1, "rb") as f:
                while (byte := f.read(1)):
                    x=x*f
                    if (x % 2) == 0:
                        y = evenFunc(x)
                        #print (x, y)
                        maxOp.append(y)
                    else:
                        y = oddFunc(x)
                        #print (x, y)
                        maxOp.append(y)
                    while y != 1:
                        if (y % 2) == 0:
                            y = evenFunc(y)
                            #print (x, y)
                            maxOp.append(y)
                        else:
                            y = oddFunc(y)
                            #print (x, y)
                            maxOp.append(y)
            maxNumber = max(maxOp)
            print(x, maxNumber)
            maxOp = []






