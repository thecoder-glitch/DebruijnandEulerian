from random import randint
from copy import deepcopy



stack1 = []
stack2 = []
data_read = open('/Users/taraghazanfari/Desktop/Week3_BENG181/dataset.txt', 'r')
def buildadjacencymatrix(data_read):
    a_list = {}
    numb = 0
    for i in data_read:
        node = i.strip('\n')
        node = node.replace(' -> ', ' ')
        node = node.split(' ')
        a_list.setdefault(node[0], [])
        for number in node[1].split(','):
            a_list[node[0]].append(number)
            numb = numb + 1
    return a_list, numb

def EulerianCycle(data_read):
    a_list, numb = buildadjacencymatrix(data_read)
    graph = {}
    graph = deepcopy(a_list)
    current = '1'
    while len(stack2) != numb:
        if graph[current] == []:
            stack2.append(current)
            current = stack1[len(stack1) - 1]
            stack1.pop()
        else:
            stack1.append(current)
            chose = randint(0, len(graph[current])-1)
            temp = deepcopy(current)
            current = graph[temp][chose]
            graph[temp].remove(current)
    start = '1'
    path = start + '->'
    for i in stack2[::-1]:
        path += (i + '->')
    return path.strip('->')



print(EulerianCycle(data_read))
