import sys
santa_location = (0,0)
robo_location  = (0,0)
houses_visited = dict()
def visit(loc):
	houses_visited[loc] = houses_visited.get(loc, 0) + 1
# visit the initial house
visit((0,0))
# follow directions and record visits as relative locations from origin
char_num = 0
with (open(sys.argv[1], "r")) as infile:
	while (True):
		char = infile.read(1)
		# determine if instruction for Santa or Robo-Santa
		# get corresponding previous location
		char_num = char_num + 1
		location = santa_location
		if (char_num % 2 == 0):
			location = robo_location
		# update location
		if not char:
			break
		elif char == '^':
			location = (location[0], location[1] + 1)
		elif char == 'v':
			location = (location[0], location[1] - 1)
		elif char == '>':
			location = (location[0] + 1, location[1])
		elif char == '<':
			location = (location[0] - 1, location[1])
		# record visit to location
		visit(location)
		# write location back out to corresponding global variable
		if (char_num % 2 == 0):
			robo_location = location
		else:
			santa_location = location
			
unique_houses_visited = len(houses_visited.keys())
print("Unique houses visited: " + str(unique_houses_visited))
