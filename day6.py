import re

input = open("day6.txt", "r")
text = input.read()
text = text.split('\n')

#time = text[0].split()[1:]
#time = [int(x) for x in time]
timeText = "".join(text[0].split()[1:])

time = int(timeText)

print(time)

#distance = text[1].split()[1:]
# distance = [int(x) for x in distance]

distanceText = "".join(text[1].split()[1:])

distance = int(distanceText)

print(time)

print(distance)

# prod = 1

#for i in range(0, len(time)):
t = time
d = distance

halfTime = t // 2
# print("halfTime", halfTime)

sum = 1 if halfTime * (t - halfTime) > d else 0

for j in range(1, halfTime):
    a = False
    b = False
    
    aTime = halfTime + j
    bTime = halfTime - j
    
    #print(aTime, bTime)
    
    if aTime * (t - aTime) > d:
        sum += 1
    else: a = True
    
    if bTime * (t - bTime) > d:
        sum += 1
    b = True
    
    if a and b:
        break
print("sum", sum)
# prod *= sum if sum > 0 else 1
    

# print(prod)
