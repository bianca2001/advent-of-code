if __name__ == '__main__':
    input = open("day15example.txt", "r")
    text = input.read()
    text = text.split(',')
    
    sum = 0
    for item in text:
        value = 0
        for char in item:
            value += ord(char)
            value *= 17
            value = value % 256
        sum += value

    print(sum)