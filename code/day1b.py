from aocd import data

def _get_fuel(module_weight):
	return (module_weight//3)-2

def get_fuel(module_weight):
	fuel = _get_fuel(module_weight)
	if _get_fuel(fuel)>0:
		fuel+=get_fuel(fuel)
	return fuel

modules = [int(x) for x in data.splitlines()]

fuel = sum([get_fuel(x) for x in modules])

print("Total fuel: {!s}".format(fuel))
