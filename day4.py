import re

input = open("day4.txt", "r")
text = input.read()
text = text.split('\n')

sum = 0

cardsCount = [1] * 200

for line, cardNr in zip(text, range(1, len(text) + 1)):
    begining = line.find(':')
    newLine = line[begining + 2:]
    newLine = newLine.strip()
    newLine = newLine.split(' | ')
    winningNumbers = re.split("   |  | ", newLine[0])
    actualNumbers = re.split("   |  | ", newLine[1])
    
    count = 0
    prod = 0
    
    for nr in actualNumbers:
        if nr in winningNumbers:
            count += 1
    
    if count > 0:
        #prod = 2 ** (count- 1)
        
        for i in range(1, count + 1):
            cardsCount[cardNr + i] += cardsCount[cardNr]
    
    #print(prod, cardsCount[cardNr])
    sum += cardsCount[cardNr]
    print(sum)
    

print(sum)