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

	def p(self):
		print('state:%s' % self.name)
		return

	def addTransform(self, token, target):
		if token in self.transTable:
			print('this token %s is already in transTable' % token)
			# make a warmming, maybe need to raise an error
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
	
	def _getNext(self, state, token):
		assert len(token)==1, 'token must be a char'
		print('get token %s' % token)
		now, nextState = state, None
		if token in now.transTable:
			nextState = now.transTable[token]
		else: # use symbol list to check,190220 OK
			symbSets = filter(isSymbKey,list(now.transTable.keys()))
			for symbSet in symbSets:
				if token in symbSet:
					nextState = now.transTable[symbSet] # transform to next state

		if nextState:
			print('from %s to %s' % (now.name, nextState.name))
			# if self.now.act: now.act() # state behavior
			return nextState
		else:
			print('this token %s is not in transTable' % token)
			# TODO: stop FSM, error end
			# stay in 'now'
			return now
		
	def step(self, token):
		self.now = self._getNext(self.now, token)
		return 
	
	def execute(self, tape):
		print('FSM is start')
		print('tape:',tape)
		self.tape = tape
		# if self.now.act:
			# self.now.act()
		for token in self.tape:
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

print('print all states')
for s in stateList:
	# print(s)
	s.p()
	print('--')

fsm = FSM(states,states['S1'])

fsm.execute('0')
fsm.execute('123')
fsm.execute('1.987')
fsm.execute('0.0')
fsm.execute('0.9')
fsm.execute('0.900')

fsm._getNext(stateList[0],'0')
fsm._getNext(stateList[0],'1')
fsm._getNext(stateList[0],'2')
fsm._getNext(stateList[1],'.')
fsm._getNext(stateList[1],'1')

