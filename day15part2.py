def printNonEmptyBoxes(boxes):
    for index, b in enumerate(boxes):
        if len(b) > 0:
            print(index, b)


if __name__ == '__main__':
    input = open("day15.txt", "r")
    text = input.read()
    text = text.split(',')
    
    boxes = [[] for i in range(256)] 
    sum = 0
    for item in text:
        equal = 0
        minus = False
        
        if '-' in item:
            minus = True
            item = item.replace('-', '')
        if '=' in item:
            equal = int(item[item.index('=') + 1:])
            item = item[:item.index('=')]
        
        value = 0
        for char in item:
            value += ord(char)
            value *= 17
            value = value % 256
        
        if minus:
            for b in boxes[value]:
                if item in b:
                    boxes[value].remove(b)
                    break
        if equal > 0:
            for index, b in enumerate(boxes[value]):
                if item in b:
                    boxes[value][index] = item + ' ' + str(equal)
                    break
            else:
                boxes[value].append(item + ' ' + str(equal))
    
    
    for indexBox, box in enumerate(boxes):
        for indexItem, item in enumerate(box):
            sum += (indexBox + 1) * (indexItem + 1) * int(item[item.index(' ') + 1:])
    
    print(sum)
    
#282736 too low