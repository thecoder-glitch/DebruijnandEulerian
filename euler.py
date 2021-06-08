infile = open('/Users/taraghazanfari/Desktop/Week3_BENG181/dataset.txt', 'r')

adj_list = {}
circuit_max = 0
for line in infile:
    node = line.strip('\n')
    node = node.replace(' -> ', ' ')
    node = node.split(' ')
    adj_list.setdefault(node[0], [])
    for number in node[1].split(','):
        adj_list[node[0]].append(number)
        circuit_max += 1
print(adj_list)