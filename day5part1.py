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
        current.extend([int(x) for x in numbers[1:]])
            
    for line in lines[1:]:
        numbers = line.split(' ')
        dest = int(numbers[0])
        source = int(numbers[1])
        length = int(numbers[2])
        #print(dest, source, length)
        maps[lines[0]].append((dest, source, length))


for list in maps.values():
    print(list)
    for c, i in zip(current, range(0, len(current))):
        for tuple in list:
            dest = tuple[0]
            source = tuple[1]
            length = tuple[2]
            
            if source <= c and c <= source + length:
                current[i] = dest + c - source
                break 

print(current)
print(min(current))


