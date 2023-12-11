import re
import time

input = open("day1.txt", "r")
text = input.read()
text = text.split('\n')
sum = 0

numbers = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

for i in text:
    first = 0
    last = 0
    
    for j in numbers.keys():
        if j in i:
            # print(j, numbers[j])
            # i = i.replace(j, numbers[j])
            
    
    print(i)
    
    for j in i:
        if j.isdigit():
            first = int(j)
            break
    
    
    for j in reversed(i):
        if j.isdigit():
            last = int(j)
            break
    
    number = first * 10 + last
    sum += number
    
    
print(sum)