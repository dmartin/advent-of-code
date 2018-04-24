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
print(curr)