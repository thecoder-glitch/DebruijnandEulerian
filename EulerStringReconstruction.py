from random import choice

data_open = open('/Users/taraghazanfari/Desktop/Week3_BENG181/dataset.txt', 'r')
data_read = data_open.read().splitlines()
k = data_read[0]
patterns = []
for i in range(1, len(data_read)):
    patterns.append(data_read[i])


def deBruijnGraph(patterns):
    dB = {}
    for i in range(len(patterns)):
        try:
            #this will add the correct DNA to the dictionary
            dB[patterns[i][:-1]].append(patterns[i][1:])
        except:
            #if it is unable to add to the dictionary in the previous way, it will add this way
            dB[patterns[i][:-1]] = [patterns[i][1:]]

    return dB

def outter(index, dB):
    return(len(dB[index]))


def BeginingNode(dB):
    for i in dB.keys():
        inner = sum([1 for x, y in dB.items() if i in y])
        if inner < outter(i, dB):
            start_n = i
            return start_n




def EulerianPathProbelm(dB):
    resulting = []
    start_n = BeginingNode(dB)
    traverse_e = [start_n]
    while len(traverse_e) != 0:
        upper = traverse_e[-1]
        if upper not in dB:
            resulting.append(traverse_e.pop())
            continue
        out_edge = dB[upper]
        if len(out_edge) > 0:
            pick_e = choice(out_edge)
            temp = list(dB[upper])
            temp.remove(pick_e)
            dB[upper] = temp
            traverse_e.append(pick_e)
        elif len(out_edge) == 0:
            resulting.append(traverse_e.pop())
    return resulting[::-1]


def PathtoGenome(path):
    finalstring = path[0]
    for i in range(1, len(path)):
        finalstring += path[i][-1]
    return finalstring


def StringReconstruction(patterns):
    dB = deBruijnGraph(patterns)
    path = EulerianPathProbelm(dB)
    text = PathtoGenome(path)
    return text

print(StringReconstruction(patterns))
