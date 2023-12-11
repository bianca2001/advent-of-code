import numpy as np
import math

if __name__ == '__main__':
    input = open("day11.txt", "r")
    text = input.read()
    text = text.split('\n')
    
    matrix = np.array([list(line) for line in text])
    print(matrix)
    
    lineExpansionPosition = []
    i = 0
    while i < len(matrix):
        if '#' in matrix[i]:
            i += 1
            continue
        
        # matrix = np.insert(matrix, i, matrix[i], axis=0)
        lineExpansionPosition.append(i)
        i += 1
    
    columnExpansionPosition = []
    i = 0
    
    while i < len(matrix[0]):
        if '#' in matrix[:,i]:
            i += 1
            continue
        
        # matrix = np.insert(matrix, i, matrix[:,i], axis=1)
        columnExpansionPosition.append(i)
        i += 1
    
    galaxyesPositions = []
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '#':
                posI = i + sum([999999 for k in range(len(lineExpansionPosition)) if lineExpansionPosition[k] < i])
                posJ = j + sum([999999 for k in range(len(columnExpansionPosition)) if columnExpansionPosition[k] < j])
                galaxyesPositions.append((posI,posJ))
    
    sum = 0
    
    for i in range(len(galaxyesPositions) - 1):
        for j in range(i + 1, len(galaxyesPositions)):
            sum += abs(galaxyesPositions[i][0] - galaxyesPositions[j][0]) + abs(galaxyesPositions[i][1] - galaxyesPositions[j][1])
            
    print(sum)
    