input = open("day5.txt", "r")
text = input.read()
text = text.split('\n\n')

#firstSegment = text[0]
#numbers = firstSegment[firstSegment.find(':') + 2:].split(' ')

#current = [int(x) for x in numbers]
current = []
maps = {"seed-to-soil map:": [], "soil-to-fertilizer map:": [], "fertilizer-to-water map:": [], \
    "water-to-light map:": [], "light-to-temperature map:": [], "temperature-to-humidity map:": [], \
        "humidity-to-location map:": []}

for segment in text:
    lines = segment.split('\n')
    
    if 'seeds:' in lines[0]:
        numbers = lines[0].split(' ')
        current.extend([(int(x), int(y)) for x,y in zip(*[iter(numbers[1:])]*2)])
        print(current)
            
    for line in lines[1:]:
        numbers = line.split(' ')
        dest = int(numbers[0])
        source = int(numbers[1])
        length = int(numbers[2])
        #print(dest, source, length)
        maps[lines[0]].append((dest, source, length))


for key, list in maps.items():
    localCurrent = current.copy()
    
    print(key)
    
    #for pair, i in zip(localCurrent, range(0, len(localCurrent))):
    while len(localCurrent) > 0:
        pair = localCurrent[0]
        print("local",localCurrent)
        
        for tuple in list:
            dest = tuple[0]
            source = tuple[1]
            length = tuple[2]
            
            offset = dest - source
            
            if source <= pair[0] and pair[0] < (source + length):
                if source + length >= pair[0] + pair[1]:
                    print("aa")
                    #current.append((dest + pair[0] - source, pair[1]))
                    current.append((pair[0] + offset, pair[1]))
                    if pair in current:
                        current.remove(pair)
                    localCurrent.remove(pair)
                else:
                    print("ab")
                    newLength = pair[0] + pair[1] - source - length
                    current.append((pair[0] + offset, pair[1] - newLength))
                    localCurrent.append((source + length, newLength))
                    if pair in current:
                        current.remove(pair)
                    localCurrent.remove(pair)
                break
                
                
            elif source < (pair[0] + pair[1]) and (pair[0] + pair[1]) < (source + length):
                print("b")
                newLength = pair[1] - (source - pair[0])
                localCurrent.append((pair[0], pair[1] - newLength))
                current.append((dest, newLength))
                if pair in current:
                    current.remove(pair)
                localCurrent.remove(pair)
                break
        else:
            if pair not in current:
                current.append(pair)
            localCurrent.remove(pair)
        
        print("current",current)
        #print(current)

print(current)
beginings = [x[0] for x in current]
print(min(beginings))