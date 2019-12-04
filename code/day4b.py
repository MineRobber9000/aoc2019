from aocd import data
import copy
DIGITS = list(range(10)) # 0,1,2,3,4,5,6,7,8,9

def passwd(ln,l=set(),oln=None):
	if oln is None: oln=ln
	if len(l)==0 and ln>=1:
		l.update([str(x) for x in DIGITS])
		return passwd(ln-1,l,oln)
	elif ln==0:
		return set([x for x in l if len(x)==oln])
	else: # l has items and ln isn't 0
		nl = l.copy()
		for paswd in l:
			last_digit = int(paswd[-1])
			for x in DIGITS:
				if x>=last_digit:
					nl.add(paswd+str(x))
		return passwd(ln-1,nl,oln)

r = [int(x) for x in data.split("-")]

def test_password(pw):
	if type(pw)!=str: pw = str(pw)
	if not len([x for x in [(c==pw[i+1] if (i+1)<len(pw) else False) if pw.count(c)==2 else False for i,c in enumerate(pw)] if x])>=1:
		return False
	return True

passwords = set(str(x) for x in range(r[0],r[1]))
possible_passwords = set(x for x in passwd(6) if test_password(x))

print(len(passwords.intersection(possible_passwords)))
