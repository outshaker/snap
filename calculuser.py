# https://zerojudge.tw/ShowProblem?problemid=d618
# abstract FSM simulation

def isSymb(x): return type(x) is str and len(x)>1
def isChar(x): return type(x) is str and len(x)==1
def isSymbKey(x): return type(x) is frozenset

class State:
	def __init__(self, name, actFunc=None, isAccept=False):
		self.name = name
		self.act = actFunc
		self.transTable = {}
		self.isAccept = isAccept
		
	def __str__(self):
		s = 'state:%s,%s\n' % (self.name,self.isAccept)
		for k in list(self.transTable.keys()):
			s += '(%s)-> %s\n' % (k,self.transTable[k].name)
		return s

	# TODO: need to remove it
	def p(self):
		print('state:%s' % self.name)
		return

	def addTransform(self, token, target):
		if token in self.transTable:
			print('this token %s is already in transTable' % token)
			# TODO: make a warmming. solution: 1. raise an error 2. make a new target to cover it

		else:
			self.transTable[token] = target

	# def isFinalState(self):
		# return len(self.transTable) == 0

	def isAcceptState(self):
		return self.isAccept

	def setAcceptable(self,b):
		self.isAccept = b

class FSM:
	def __init__(self, states, startState):
		self.states = states
		self.now = startState
		self.start = startState # restore this value
		self.loader = ''
		
	def _getNext(self, state, token):
		assert len(token)==1, 'token must be a char'
		# print('get token %s' % token)
		now, nextState = state, None
		if token in now.transTable:
			nextState = now.transTable[token]
		else: # use symbol list to check,190220 OK
			symbSets = filter(isSymbKey,list(now.transTable.keys()))
			for symbSet in symbSets:
				if token in symbSet:
					nextState = now.transTable[symbSet] # transform to next state

		if nextState:
			# print('from %s to %s' % (now.name, nextState.name))
			# if self.now.act: now.act() # state behavior
			return nextState
		else:
			print('this token %s is not in transTable' % token)
			# TODO: stop FSM, error end
			# stay in 'now'
			return None
	
	def reset(self):
		self.now = self.start
		self.loader = ''
		return
	
	def step(self, token):
		t = self._getNext(self.now, token)
		if t:
			self.now = t
			self.loader += token
		return 
	
	def dump(self):
		x = self.loader
		self.reset()
		return x
	
	def val(self):
		return self.loader
	
	def execute(self, tape):
		print('FSM is start')
		print('tape:',tape)
		self.reset() # init
		# if self.now.act:
			# self.now.act()
		for token in tape:
			self.step(token)
			
		if self.now.isAcceptState():
			print('Accept')
		else:
			print('Deny!')
		print('FSM is finish')


Symbs={
'd09':{'0','1', '2', '3', '4', '5', '6', '7', '8', '9'},
'd19':{'1', '2', '3', '4', '5', '6', '7', '8', '9'},
}

Stats={
'S1':{'0':'S2', 'd19':'S3','accpet':False},
'S2':{'.':'S5','accpet':True},
'S3':{'d09':'S4','.':'S5','accpet':True},
'S4':{'d09':'S4','.':'S5','accpet':True},
'S5':{'d09':'S6','accpet':False},
'S6':{'0':'S7', 'd19':'S6','accpet':True},
'S7':{'0':'S7', 'd19':'S6','accpet':False}
}

states={} #{'S1':State('S1'), ... }
stateList=[] #[State('S1'), ... ]

# build all state in a dict{}
for x in list(Stats.keys()):
	s = State(x)
	states[x] = s
	stateList.append(s)

# addTransform and setAcceptable
# TODO: package this code to method.
# TODO: need error detect. 
for m in list(Stats.items()): # m [triple], (state name, [dict])
	statn,statobj = m[0],m[1]
	for token2target in list(statobj.items()): # m[1] [dict], token2target [triple] (token,target)
		k,v = token2target[0],token2target[1]
		if k is 'accpet':
			states[statn].setAcceptable(v)
		elif isChar(k):
			states[statn].addTransform(k, states[v])
		elif isSymb(k):
			states[statn].addTransform(frozenset(Symbs[k]), states[v])
		else: pass

fsm = FSM(states,states['S1'])

# little calculuser
from getkey import getkey, keys

N={'N0','N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9','PERIOD'} #0-9.
OP={'PLUS', 'MINUS', 'ASTERISK', 'SLASH'} # +-*/
END={'EQUALS', 'SPACE','ENTER'} # =
ESC={'ESC'}

isNum = lambda x: keys.name(x) in N
isOp = lambda x: keys.name(x) in OP
isEnd = lambda x: keys.name(x) in END
isEsc = lambda x: keys.name(x) in ESC

Opfunc = {
'+': lambda x,y: x+y,
'-': lambda x,y: x-y,
'*': lambda x,y: x*y,
'/': lambda x,y: x/y,
}

mem1 = None
mem2 = None
opcode = None
s='S0'
while True:
	# get token
	# t = getkey(blocking=False)
	t = getkey(blocking=True)
	if isNum(t): # deal num
		if s=='S0':
			print('S0->S1')
			fsm.reset()
		elif s=='S2':
			print('S2->S1')
			fsm.reset()
		elif s=='S1':
			print('S1->S1')
			pass
		else: print('Exception: from unkonwn state.')
		fsm.step(t)
		s='S1'
	elif isOp(t): # deal op
		if s=='S0':
			print('S0->S2')
			mem1 = 0
		elif s=='S2':
			print('S2->S2')
		elif s=='S1':
			print('S1->S2')
			if not mem1:
				mem1 = float(fsm.dump())
				print('load mem1',mem1)
			elif mem1 and opcode:
				mem2 = float(fsm.dump())
				print('load mem2',mem2)
				if mem2==0 and opcode=='/': # check Exception
					print('Exception: x/0')
					mem1=0
				else: 
					mem1 = Opfunc[opcode](mem1,mem2)
					print(mem1)
			elif mem1 and (not opcode):
				print('Exception: no op code')
			else:
				print('Exception: unkonwn error')
		opcode=t
		print('load opcode',opcode)
		s='S2'
	elif isEnd(t):
		print('->S0')
		# make last op
		if s=='S1' and mem1 and opcode:
			mem2 = float(fsm.dump())
			print('load mem2',mem2)
			if mem2==0 and opcode=='/': # check Exception
				print('Exception: x/0')
				mem1=0
			else: 
				mem1 = Opfunc[opcode](mem1,mem2)
				print(mem1)
		s='S0'
	elif isEsc(t):
		break
	else:
		# do nothing
		pass
	print(fsm.val(),'m1:',mem1,'op:',opcode)
