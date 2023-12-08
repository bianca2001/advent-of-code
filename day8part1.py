import linkedList

input = open("day8.txt", "r")
text = input.read()
text = text.split('\n')

commandOrder = text[0]

text = text[2:]
data = {}

for line in text:
    starting = line.split(' = ')
    directions = starting[1][1:-1].split(', ')
    
    data[starting[0]] = directions


current = 'AAA'
posCommanda = 0
counter = 0

while current != 'ZZZ':
    command = commandOrder[posCommanda]
    print(current)
    if command == "R":
        current = data[current][1]
    elif command == "L":
        current = data[current][0]

    counter += 1
    posCommanda = (posCommanda + 1) % len(commandOrder)

print(counter)
    


