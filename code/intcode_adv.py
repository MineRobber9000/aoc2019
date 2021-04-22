def pad(s,l,c="0"):
	return (s+(c*l))[:l]

def intput():
	v = None
	while v is None:
		try:
			v = int(input("? "))
		except KeyboardInterrupt: raise
		except: pass
	return v

class ParameterTypes:
	READ=1
	WRITE=2

class Computer:
	OPCODE_LENGTHS = {1: 3, 2: 3, 3: 1, 4: 1}
	OPCODE_PARAMS = {1: [ParameterTypes.READ,ParameterTypes.READ,ParameterTypes.WRITE], 2: [ParameterTypes.READ,ParameterTypes.READ,ParameterTypes.WRITE], 3: [ParameterTypes.WRITE], 4: [ParameterTypes.READ]}
	OPCODE_DEFAULTS = {1: list("000"), 2: list("000"), 3: list("0"), 4: list("0")}
	def __init__(self,prog,force_param_types={}):
		if type(prog)==str:
			prog = [int(x.strip()) for x in prog.split(",") if x.strip()]
		self.memory = {i: prog[i] for i in range(len(prog))}
		self.force_param_types = force_param_types
	def parse_opcode(self,mem):
		opcode = mem%100
		params = list(pad(str(mem//100)[::-1],self.OPCODE_LENGTHS.get(opcode,0)))
		return int(opcode), params
	def grab_value(self,addr,mode):
		if mode=="0":
			val = self.memory[self.memory[addr]]
		elif mode=="1":
			val = self.memory[addr]
		return addr+1, val
	def evaluate(self):
		pc = 0
		while pc<len(self.memory) and self.memory[pc]!=99:
			opcode, params = self.parse_opcode(self.memory[pc])
			pc+=1
			if opcode in self.force_param_types:
				params = self.force_param_types[opcode]
			if opcode in self.OPCODE_LENGTHS:
				values = []
				for i in range(len(params)):
					mode = params[i]
					type = self.OPCODE_PARAMS[opcode]
					if type==ParameterTypes.WRITE:
						mode = "1" # because of how I'm using it, I need the actual value at the address
					pc, v = self.grab_value(pc,mode)
					values.append(v)
				if opcode==1:
					self.memory[values[2]]=values[0]+values[1]
				elif opcode==2:
					self.memory[values[2]]=values[0]*values[1]
				elif opcode==3:
					self.memory[values[0]]=intput()
				elif opcode==4:
					print(values[0])
			else:
				raise Exception("Unknown opcode {:02d} at {:02d}".format(self.memory[pc],pc))
