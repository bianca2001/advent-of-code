import math

input = open("day8.txt", "r")
text = input.read()
text = text.split('\n')

commandOrder = text[0]

text = text[2:]
data = {}

current = []

for line in text:
    starting = line.split(' = ')
    directions = starting[1][1:-1].split(', ')
    
    data[starting[0]] = directions

    if starting[0].endswith('A'):
        current.append(starting[0])


def getNext(current, command):
    if command == "R":
        result = data[current][1]
        return result
    elif command == "L":
        result = data[current][0]
        return result


repeatigInterval = []
posCommanda = 0

for c in current:
    repeating = 0
    startValue = c
    posCommanda = 0
    foundEnd = 0

    element = c

    while foundEnd < 2:
        command = commandOrder[posCommanda]
        element = getNext(element, command)
        
        if foundEnd == 0:
            if element.endswith('Z'):
                foundEnd += 1
        elif foundEnd == 1:
            if element.endswith('Z'):
                foundEnd += 1
            repeating += 1

        posCommanda = (posCommanda + 1) % len(commandOrder)

    repeatigInterval.append(repeating)

print(math.lcm(*repeatigInterval))