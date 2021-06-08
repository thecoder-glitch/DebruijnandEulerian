data_open = open('/Users/taraghazanfari/Desktop/Week3_BENG181/dataset.txt', 'r')
data_read = data_open.read().splitlines()
k = int(data_read[0])
text = data_read[1]


def buildsequence(k, text):
    kmers = []
    for i in range(0, len(text)-k+1):
        kmers.append(text[i:i+k])
    return kmers

def getedge(k, text):
    nodes = []
    edges = []
    size = len(text)
    for i in range(0, size-k+1):
        nodes.append(text[i:i+k])
    for i in nodes:
        edges.append(buildsequence(k-1, i))
    return edges


def DeBruijn(k, text):
    final_graph = {}
    edges1 = getedge(k, text)

    for i in edges1:
        final_graph[i[0]]=[]
    for i in edges1:
        final_graph[i[0]].append(i[1])

    return final_graph


def printDeBrujin(final_graph):
    for i in final_graph:
        if final_graph[i] not in []:
            print(i+ ' -> ' + str(final_graph[i])[1:-1].replace("'", ''))

finalGraph = DeBruijn(k, text)
printDeBrujin(finalGraph)

