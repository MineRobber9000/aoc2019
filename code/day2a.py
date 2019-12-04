import intcode
from aocd import data

comp = intcode.Computer(data)
comp.memory[1]=12
comp.memory[2]=2
comp.evaluate()
print(comp.memory[0])
