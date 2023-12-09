if __name__ == '__main__':
    input = open("day09.txt", "r")
    text = input.read()
    text = text.split('\n')
    
    allResults = []
    
    for line in text:
        numbers = line.split(' ')
        numbers = [[int(x) for x in numbers]]
        
        numbers.append([y-x for x, y in zip(numbers[0][:-1], numbers[0][1:])])
        i = 1
        while not all(x == 0 for x in numbers[i]):
            i += 1
            numbers.append([y-x for x, y in zip(numbers[i - 1][:-1], numbers[i - 1][1:])])
        
        allResults.append(numbers)
        
    print(allResults)
    
    sum = 0
    for result in allResults:
        lastValue = 0
        
        for line in reversed(result):
            lastValue = line[0] - lastValue
            print(lastValue)
        
        sum += lastValue

    print(sum)