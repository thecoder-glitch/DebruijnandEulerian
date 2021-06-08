from random import choice

data_read = open('/Users/taraghazanfari/Desktop/Week3_BENG181/dataset.txt', 'r')
dB = {}
for i in data_read:
    node = i.strip('\n')
    node = node.replace(' -> ', ' ').split(' ')
    #node = node.split(' ')
    dB.setdefault(node[0], [])
    for number in node[1].split(','):
        dB[node[0]].append(number)

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
        starting_point = ''
        final_result = starting_point + '->'
        for x in resulting[::-1]:
            final_result += (x + '->')
        print(final_result)
        return final_result.strip('->')
    #return resulting[::-1]
    #holds the final result
    #resulting = []
    #vertex = StartingVertex(graph)
    #edge = [vertex]
    #while len(edge) != 0:
        #starting = edge[-1]
        #if starting not in graph:
            #resulting.append(edge.pop())
            #continue
        #edge2 = graph[starting]
        #print(list(edge2))
        #if len(edge2) > 0:
            #e = choice(edge2)
            #graph[starting].remove(e)
            #edge.append(e)
        #elif len(edge2) == 0:
            #resulting.append(edge.pop())
    #starting_point = ''
    #final_result = starting_point + '->'
    #for x in resulting[::-1]:
        #final_result += (x + '->')
    #return final_result.strip('->')



starting_point = ''
    final_result = starting_point + '->'
        for x in resulting[::-1]:
            final_result += (x + '->')
        print(final_result)
        return final_result.strip('->')
