import intcode
from aocd import data

def try_noun_verb(noun,verb):
	comp = intcode.Computer(data)
	comp.memory[1]=noun
	comp.memory[2]=verb
	comp.evaluate()
	return comp.memory[0]==19690720

for noun in range(0,100):
	for verb in range(0,100):
		if try_noun_verb(noun,verb):
			print("SOLUTION: {:02d} {:02d} ({:d})".format(noun,verb,(noun*100+verb)))
