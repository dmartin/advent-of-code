import sys
import re
import collections

infile = sys.stdin.read().strip().split('\n')

# For each line, extract the node and its children
Entry = collections.namedtuple('Entry', ['node', 'weight', 'children'])
entries = []
p = re.compile(r'^(\w*) \((\d*)\)( -> )?(.*)?$')
for line in infile:
    m = p.search(line).groups()
    e = Entry(m[0], m[1], m[3])
    entries.append(e)

# Build a child -> parent lookup table
parent = {}
for entry in entries:
    children = entry.children.split(', ')
    for child in children:
        parent[child] = entry.node

# Traverse the table to the root
curr = list(parent.keys())[0]
while(True):
    try:
        curr = parent[curr]
    except KeyError:
        break
root = curr

# Build a node weight lookup table
weights = {}
for entry in entries:
    weights[entry.node] = int(entry.weight)

# Build a parent -> child lookup table
children = collections.defaultdict(list)
for entry in entries:
    if (entry.children != ''):
        children[entry.node] = entry.children.split(', ')

def totalweight(node):
    childsum = 0
    for child in children[node]:
        childsum += totalweight(child)
    return childsum + weights[node]

# For all nodes, see if their children have the same weights
for entry in entries:
    if (entry.children == ''):
        continue
    weightsFound = set()
    for child in entry.children.split(', '):
        weightsFound.add(totalweight(child))
    if (len(weightsFound) != 1):
        print("node {} has children with weights:".format(entry.node))
        for child in entry.children.split(', '):
            print("{}: {}".format(child, totalweight(child)))

# From here, the mismatched weight in the overall smallest set needs its weight adjusted.