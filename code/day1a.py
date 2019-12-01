from aocd import data

def get_fuel(module_weight):
	return (module_weight//3)-2

modules = [int(x) for x in data.splitlines()]

fuel = sum([get_fuel(x) for x in modules])

print("Total fuel: {!s}".format(fuel))
