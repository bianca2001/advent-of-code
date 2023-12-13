def isMirrorHorizontal(i, j, pattern):
    for k in range(1, min(i, len(pattern) - j)):
        if pattern[i - k] != pattern[j + k]:
            print(i - k, j + k)
            return False
        else:
            print(i - k, j + k)
            print(pattern[i - k], pattern[j + k])
    return True


def isMirrorVertical(i, j, pattern):
    for k in range(1, min(i, len(pattern) - j)):
        if pattern[i - k] != pattern[j + k]:
            return False
    return True


if __name__ == '__main__':
    input = open("day13example.txt", "r")
    text = input.read()
    text = text.split('\n\n')
    
    verticalSum = 0
    horizontalSum = 0
    for pattern in text:
        pattern = pattern.split('\n')
        
        #print(len(pattern))
        for i, line in enumerate(pattern, start=1):
            if line == pattern[i - 1]:
                if isMirrorHorizontal(i - 1, i, pattern):
                    horizontalSum += i - 1
                    break
        print(horizontalSum)
        #len(pattern[0])
        # for i in range(len(pattern[0]) - 1):
        #     len(pattern[0])
            # if pattern[:][i] == pattern[:][i + 1]:
            #     print(pattern[:][i], pattern[:][i + 1])
            #     if isMirrorVertical(i, i + 1, pattern):
            #         horizontalSum += 1