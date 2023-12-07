from functools import cmp_to_key

input = open("day7.txt", "r")
text = input.read()
text = text.split('\n')

cards = []

for line in text:
    values = line.split()
    
    cards.append((values[0], values[1]))
    
def is_a_bigger_than_b(a, b):
    if a == b:
        return 0
    if a == "A":
        return 1
    if b == "A":
        return -1
    if a == "K":
        return 1
    if b == "K":
        return -1
    if a == "Q":
        return 1
    if b == "Q":
        return -1
    

def get_bigger_letter(a, b):
    for letterA, letterB in zip(a, b):
        if letterA == letterB:
            continue
        if letterA == "J":
            return -1
        if letterB == "J":
            return 1
        if letterA.isdigit() and not letterB.isdigit(): 
            return -1
        if letterB.isdigit() and not letterA.isdigit():
            return 1
        if letterA.isdigit() and letterB.isdigit():
            if int(letterA) > int(letterB):
                return 1
            elif int(letterA) < int(letterB):
                return -1
            else:
                continue
        if is_a_bigger_than_b(letterA, letterB) == 1:
            return 1
        elif is_a_bigger_than_b(letterA, letterB) == -1:
            return -1 
    return 0 


def cmp_items(a, b):
    a = a[0]
    b = b[0]
    
    frequencyA = {}
    
    print(a, b)
    
    for letter in a:
        frequencyA[letter] = frequencyA.get(letter, 0) + 1
    
    jokerA = frequencyA.get("J", 0)
    frequencyA.pop("J", None)
    
    sortedFrequencyA = sorted(frequencyA.items(), key=lambda x: x[1], reverse=True)
    
    frequencyB = {}
    for letter in b:
        frequencyB[letter] = frequencyB.get(letter, 0) + 1
    
    jokerB = frequencyB.get("J", 0)
    frequencyB.pop("J", None)
    
    sortedFrequencyB = sorted(frequencyB.items(), key=lambda x: x[1], reverse=True)
    
    fiveA = 1 if jokerA == 5 or sortedFrequencyA[0][1] + jokerA == 5 else 0
    fiveB = 1 if jokerB == 5 or sortedFrequencyB[0][1] + jokerB == 5 else 0
    
    if fiveA != fiveB:
        return fiveA - fiveB
    elif fiveA == 1:
        return get_bigger_letter(a, b)
    
    fourA = 1 if sortedFrequencyA[0][1] + jokerA == 4 else 0
    fourB = 1 if sortedFrequencyB[0][1] + jokerB == 4 else 0
    
    if fourA != fourB:
        return fourA - fourB
    elif fourA == 1:
        return get_bigger_letter(a, b)
    
    fullhouseA = 1 if (sortedFrequencyA[0][1] + jokerA == 3 and sortedFrequencyA[1][1] == 2) \
        or (sortedFrequencyA[0][1] == 3 and sortedFrequencyA[1][1] + jokerA == 2) else 0    
    fullhouseB = 1 if (sortedFrequencyB[0][1] + jokerB == 3 and sortedFrequencyB[1][1] == 2) \
        or (sortedFrequencyB[0][1] == 3 and sortedFrequencyB[1][1] + jokerB == 2) else 0
    
    print("fullhouseA", fullhouseA) 
    print(sortedFrequencyA[0][1], sortedFrequencyA[1][1])
    print("fullhouseB", fullhouseB)
    
    if fullhouseA != fullhouseB:
        return fullhouseA - fullhouseB
    elif fullhouseA == 1:
        return get_bigger_letter(a, b)
    
    threeA = 1 if sortedFrequencyA[0][1] + jokerA == 3 else 0
    threeB = 1 if sortedFrequencyB[0][1] + jokerB == 3 else 0
    
    if threeA != threeB:
        return threeA - threeB
    elif threeA == 1:
        return get_bigger_letter(a, b)
    
    twoPairA = 1 if sortedFrequencyA[0][1] == 2 and sortedFrequencyA[1][1] + jokerA == 2 else 0
    twoPairB = 1 if sortedFrequencyB[0][1] == 2 and sortedFrequencyB[1][1] + jokerB == 2 else 0
    
    if twoPairA != twoPairB:
        return twoPairA - twoPairB
    elif twoPairA == 1:
        return get_bigger_letter(a, b)
    
    onePairA = 1 if sortedFrequencyA[0][1] + jokerA == 2 else 0
    onePairB = 1 if sortedFrequencyB[0][1] + jokerB == 2 else 0
    
    if onePairA != onePairB:
        return onePairA - onePairB
    elif onePairA == 1:
        return get_bigger_letter(a, b)
    
    return get_bigger_letter(a, b) 

compareCards = cmp_to_key(cmp_items)

cards.sort(key=compareCards)
print(len(cards))
print(cards)
count = 1
sum = 0
for card in cards:
    sum += int(card[1]) * count
    count += 1

print(sum)