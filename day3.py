input = open("day3.txt", "r")
text = input.read()
text = text.split('\n')

# sum = 0
# directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]

# for line, index in zip(text, range(0, len(text))):
#     i = 0
#     while i < len(line):
#         print(i)
#         if line[i].isdigit():
#             beginDigit = i
#             endDigit = i
            
#             while(endDigit + 1 < len(line) and line[endDigit + 1].isdigit()):
#                 endDigit += 1

#             for dir in directions:
#                 for j in range(beginDigit, endDigit + 1):
#                     newPosX = index + dir[0]
#                     newPosY = j + dir[1]
                    
#                     if newPosX < 0 or newPosX >= len(text) or newPosY < 0 or newPosY >= len(line):
#                         continue
                    
#                     if text[newPosX][newPosY] != '.' and not text[newPosX][newPosY].isdigit():
#                         number = int(line[beginDigit:endDigit + 1])
#                         sum += number
#                         i = endDigit
#                         break
#                 else:
#                     continue
#                 break
        
#         i += 1

# print(sum)


stars = [(i, j) for line, i in zip(text, range(0, len(text))) for x, j in zip(line, range(0, len(line))) if x == '*']

sum = 0

directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]

for pos in stars:
    count = 0
    numbers = [0, 0]
    for dir in directions:
        newPosX = pos[0] + dir[0]
        newPosY = pos[1] + dir[1]
        
        if text[newPosX][newPosY].isdigit():
            count += 1
            print(text[newPosX][newPosY])
            beginDigit = (newPosX, newPosY)
            endDigit = (newPosX, newPosY)
            
            while(beginDigit[1] - 1 >= 0  and text[beginDigit[0]][beginDigit[1] - 1].isdigit()):
                beginDigit = (beginDigit[0], beginDigit[1] - 1)
            
            while(endDigit[1] + 1 < len(text[0]) and text[endDigit[0]][endDigit[1] + 1].isdigit()):
                endDigit = (endDigit[0], endDigit[1] + 1)
    
            number = text[beginDigit[0]][beginDigit[1]:endDigit[1] + 1]
            print(text[beginDigit[0]])
            text[beginDigit[0]] = text[beginDigit[0]][0:beginDigit[1]] + "." * len(number) + text[beginDigit[0]][endDigit[1] + 1:]
            print(text[beginDigit[0]])
            numbers[count - 1] = int(number)
    
    if count == 2:
        print(numbers)
        sum += numbers[0] * numbers[1]
        
#print(text)
print(sum)
