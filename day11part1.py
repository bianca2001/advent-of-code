import numpy as np
import math

if __name__ == '__main__':
    input = open("day11.txt", "r")
    text = input.read()
    text = text.split('\n')
    
    matrix = np.array([list(line) for line in text])
    print(matrix)
    
    i = 0
    while i < len(matrix):
        if '#' in matrix[i]:
            i += 1
            continue
        
        matrix = np.insert(matrix, i, matrix[i], axis=0)
        i += 2
    
    i = 0
    
    while i < len(matrix[0]):
        if '#' in matrix[:,i]:
            i += 1
            continue
        
        matrix = np.insert(matrix, i, matrix[:,i], axis=1)
        i += 2
    
    galaxyesPositions = []
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '#':
                galaxyesPositions.append((i,j))
    
    sum = 0
    
    for i in range(len(galaxyesPositions) - 1):
        for j in range(i + 1, len(galaxyesPositions)):
            sum += abs(galaxyesPositions[i][0] - galaxyesPositions[j][0]) + abs(galaxyesPositions[i][1] - galaxyesPositions[j][1])
            
    print(sum)
    