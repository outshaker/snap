"""
exp -> exp op term
	| exp xop term
	| term

term -> term xop factor
	| factor

factor -> number
	| (exp)
	
op -> '+' | '-'
xop -> '*' | '/'
number -> digit+
digit -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
"""

# Simulator for grammar generation
# make branch by manual or random
# make number  by random
# make op/xop by random

import random as r

grammar= {
	"exp":[["term"],
		["exp","op","term"],
		["exp","xop","term"]],
	"term":[["factor"],
		["term","xop","factor"]],
	"factor":[["number"],
		["(","exp",")"]],
	"number":[("digit","+")],
	"op":['symbolTable',"+-"],
	"xop":['symbolTable',"*/"],
	"digit":['symbolTable',"1234567890"]}

def _isNonTerminal(t):
	return t in grammar

def _hasBranchs(t):
	return len(grammar.get(t))>1 and type(grammar.get(t)[0]) is list

def _isSymbolToken(t):
	return (t in grammar) and (grammar[t][0] == 'symbolTable')

def _isLoop(t):
	return type(t) is tuple

# expand (token,repeat) to [token, ...]
def _doLoop(t):
	if t[1]=='+': return [t[0]] * r.randrange(1,8)
	elif t[1]=='*': return [t[0]] * r.randrange(0,8)
	elif t[1]=='?': return [t[0]] * r.randrange(0,1)
	elif type(t[1]) is int and type(t[2]) is int: return [t[0]] * r.randrange(t[1],t[2])
	else: return [t[0]]

def ask(seq):
	if type(seq) is list:
		# print branch and choose one
		i=int(input(seq))-1 # make i start from 1, shift 1 to list index
		if seq[i]: return seq[i]
		else: return seq[0]
	else:
		return seq

def gen(tokens):
	for i in range(len(tokens)):
		t = tokens[i]
		if _isNonTerminal(t):
			next = 0
			if _hasBranchs(t):
				#next = r.choice(grammar[t]) # choice a branch
				next = ask(grammar[t]) # manual choice
			elif _isSymbolToken(t):
				next = r.choice(grammar[t][1]) # choice a char
			else:
				next = grammar[t]
			
			for j in range(len(next)): # deal loop token
				if _isLoop(next[j]):
					next = _doLoop(next[j]) # expand loop
			tokens[i:i+1] = next
			print(tokens)
			return True
		else:
			pass
		if i == len(tokens)-1:
			print('end')
			return False

t=["exp"]
count=0
while gen(t):
	count+=1
	if count==50:
		print('count to 50, test end')
		break
