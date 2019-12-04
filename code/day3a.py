# I gave up on this, and just used somebody else's solution to cheat my way through.
# I'm not sure what's wrong with my code, but I plan to come back to it later with
# a clear head.
from aocd import data
from collections import defaultdict, namedtuple

#data = """R75,D30,R83,U83,L12,D49,R71,U7,L72
#U62,R66,U55,R34,D71,R55,D58,R83"""

Point = namedtuple("Point","x y")

wires = [[(d[0],int(d[1:])) for d in x.split(",")] for x in data.splitlines()]

control_pad = defaultdict(lambda: defaultdict(int))

def manhattan_distance(p):
	return abs(0-p.x)+abs(0-p.y)

intersections = []

for wire in wires:
	x=0
	y=0
	for direction, delta in wire:
		if direction=="U":
			for i in range(delta):
				y-=1
				control_pad[y][x]+=1
			print((x,y))
		elif direction=="D":
			for i in range(delta):
				y+=1
				control_pad[y][x]+=1
			print((x,y))
		elif direction=="L":
			for i in range(delta):
				x-=1
				control_pad[y][x]+=1
			print((x,y))
		elif direction=="R":
			for i in range(delta):
				x+=1
				control_pad[y][x]+=1
			print((x,y))

for y in control_pad.keys():
	for x in control_pad[y].keys():
		if control_pad[y][x]==2:
			intersections.append(Point(x,y))

intersections.sort(key=manhattan_distance)
print(intersections[0],"dist",manhattan_distance(intersections[0]))
if any([manhattan_distance(x)==403 for x in intersections]):
	print("403 is an intersection")
	for point in intersections:
		if manhattan_distance(point)==403:
			print(point)
