import re

input = open("day2.txt", "r")
text = input.read()
text = text.split('\n')

sum = 0
id = 0

for line in text:
    indexStart = line.index(':')
    line = line[indexStart + 2:]
    
    game = line.split('; ')
    
    
    
    id += 1
    possible = True
    maxCubes = {"red": "0", "green": "0", "blue": "0"}
    
    for round in game:
        
        aux = re.split(", | ", round)
        print(aux)
        cubes = {}
        color = ""
        for number, color in zip(*[iter(aux)]*2):
            cubes[color] = number
        
        # print(cubes)
        # if cubes.get("red") and int(cubes.get("red")) > 12 or cubes.get("green") and int(cubes.get("green")) > 13 or \
        #         cubes.get("blue") and int(cubes.get("blue")) > 14:
            
        #     possible = False
        #     break
        
        if cubes.get("red") and int(cubes.get("red")) > int(maxCubes["red"]):
            maxCubes["red"] = cubes["red"]
        
        if cubes.get("green") and int(cubes.get("green")) > int(maxCubes["green"]):
            maxCubes["green"] = cubes["green"]
        
        if cubes.get("blue") and int(cubes.get("blue")) > int(maxCubes["blue"]):
            maxCubes["blue"] = cubes["blue"]
        
        
    
    if possible:
        print("possible")
        sum += int(maxCubes["red"]) * int(maxCubes["green"]) * int(maxCubes["blue"])
    
    
    
print(sum)
            