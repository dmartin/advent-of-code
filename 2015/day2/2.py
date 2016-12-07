import sys
total_paper = 0
total_ribbon = 0
with (open(sys.argv[1], "r")) as infile:
	for line in infile:
		# put l/w/h in order by size
		values = line.split('x')
		values = [int(i) for i in values]
		values.sort()
		# get amount of wrapping paper for package
		surface_area = 2*values[0]*values[1] + 2*values[1]*values[2] + 2*values[2]*values[0]
		extra_area = values[0] * values[1] # guaranteed to be smallest side
		total_paper = total_paper + surface_area + extra_area
		# get amount of ribbon for package
		ribbon_length = 2*values[0] + 2*values[1]
		bow_length = values[0] * values[1] * values[2]
		total_ribbon = total_ribbon + ribbon_length + bow_length
print("Total square feet of wrapping paper: {0}\nTotal feet of ribbon: {1}".format(total_paper, total_ribbon))
