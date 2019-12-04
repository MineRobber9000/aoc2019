class Computer:
	def __init__(self,prog):
		if type(prog)==str:
			prog = [int(x.strip()) for x in prog.split(",") if x.strip()]
		self.memory = prog
	def evaluate(self):
		pc = 0
		while pc<len(self.memory) and self.memory[pc]!=99:
			if self.memory[pc]==1:
				from_, to_, store = self.memory[pc+1:pc+4]
				self.memory[store] = self.memory[from_]+self.memory[to_]
				pc+=4
			elif self.memory[pc]==2:
				from_, to_, store = self.memory[pc+1:pc+4]
				self.memory[store] = self.memory[from_]*self.memory[to_]
				pc+=4
			else:
				raise Exception("Unknown opcode {:02d} at {:02d}".format(self.memory[pc],pc))
