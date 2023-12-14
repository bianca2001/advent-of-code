if __name__ == '__main__':
    input = open("day14example.txt", "r")
    text = input.read()
    text = text.split('\n')
    
    sum = 0
    for k in range(500):
        #north
        for j in range(len(text[0])):
            currentRockPos = 0
            for i in range(len(text)):
                #print(i, j)
                if text[i][j] == '#':
                    currentRockPos = i + 1
                elif text[i][j] == 'O':
                    #text[currentRockPos][j] = 'O'
                    temp = list(text[i])
                    temp[j] = '.'
                    text[i] = ''.join(temp)
                    temp = list(text[currentRockPos])
                    temp[j] = 'O'
                    text[currentRockPos] = ''.join(temp)
                    currentRockPos += 1
        
        # for i in range(len(text)):
        #     print(text[i])
        # print()
        
        #west
        for i in range(len(text)):
            currentRockPos = 0
            for j in range(len(text[0])):
                #print(i, j)
                if text[i][j] == '#':
                    currentRockPos = j + 1
                elif text[i][j] == 'O':
                    #text[i][currentRockPos] = 'O'
                    temp = list(text[i])
                    temp[j] = '.'
                    temp[currentRockPos] = 'O'
                    text[i] = ''.join(temp)
                    currentRockPos += 1
        
        # for i in range(len(text)):
        #     print(text[i])
        # print()
        
        #south
        for j in range(len(text[0])):
            currentRockPos = len(text) - 1
            for i in reversed(range(len(text))):
                #print(i, j)
                if text[i][j] == '#':
                    currentRockPos = i - 1
                elif text[i][j] == 'O':
                    #text[currentRockPos][j] = 'O'
                    #text[i][j] = '.'
                    temp = list(text[i])
                    temp[j] = '.'
                    text[i] = ''.join(temp)
                    temp = list(text[currentRockPos])
                    temp[j] = 'O'
                    text[currentRockPos] = ''.join(temp)
                    currentRockPos -= 1
        
        # for i in range(len(text)):
        #     print(text[i])
        # print()
        
        #east
        for i in range(len(text)):
            currentRockPos = len(text[0]) - 1
            for j in reversed(range(len(text[0]))):
                #print(i, j)
                if text[i][j] == '#':
                    currentRockPos = j - 1
                elif text[i][j] == 'O':
                    #text[i][currentRockPos] = 'O'
                    #text[i][j] = '.'
                    temp = list(text[i])
                    temp[j] = '.'
                    temp[currentRockPos] = 'O'
                    text[i] = ''.join(temp)
                    currentRockPos -= 1
        
        for i in range(len(text)):
            print(text[i])
        print()
    
    
    sum = 0
    for j in range(len(text[0])):
            currentRockPos = len(text)
            for i in range(len(text)):
                #print(i, j)
                if text[i][j] == '#':
                    currentRockPos = len(text) - i - 1
                elif text[i][j] == 'O':
                    sum += currentRockPos
                    currentRockPos -= 1
    print(sum)