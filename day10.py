goingNorthPipes = {'|': (-1, 0), '7':(0, -1), 'F':(0, 1)}
goingEstPipes = {'-': (0, 1), 'J':(-1, 0), '7':(1, 0)}
goingSouthPipes = {'|': (1, 0), 'J':(-1, 0), 'L':(0, 1)}
goingWestPipes = {'-': (0, -1), 'L':(-1, 0), 'F':(1, 0)}
matrix = []
start = (0,0)

#go in the direction and then 
def searchForPath(current, directionPipes):
    aux = directionPipes[matrix[current[0]][current[1]]] 
    
    while current != start:
        pass


if __name__ == '__main__':
    input = open("day10example1.txt", "r")
    text = input.read()
    text = text.split('\n')
    
    
    for line in text:
        if 'S' in line:
            start = (matrix.index(line), line.index('S'))
        matrix.append(line)
    
    current = start
    
    if current in goingNorthPipes:
        searchForPath(matrix[current[0] - 1][current[1]], goingNorthPipes)