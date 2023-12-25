import re
import networkx as nx

### PART 1 ###

G = nx.Graph()
with open('input.txt', 'r') as f:
    for line in f:
        l = re.split(': | ', line.strip())
        a = l[0]
        for b in l[1:]:
            G.add_edge(a, b, weight=1)

# Stoer–Wagner algorithm
# https://en.wikipedia.org/wiki/Stoer%E2%80%93Wagner_algorithm
cut_value, partition = nx.stoer_wagner(G)
assert cut_value == 3
print(len(partition[0]) * len(partition[1]))

### PART 2 ###
