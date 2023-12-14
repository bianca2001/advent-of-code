if __name__ == '__main__':
    input = open("day14example.txt", "r")
    text = input.read()
    text = text.split('\n')
    
    sum = 0
    
    for j in range(len(text[0])):
        currentRockPos = len(text)
        for i in range(len(text)):
            print(i, j)
            if text[i][j] == '#':
                currentRockPos = len(text) - i - 1
            elif text[i][j] == 'O':
                sum += currentRockPos
                currentRockPos -= 1
    
    print(sum)