# https://zerojudge.tw/ShowProblem?problemid=d618
# abstract FSM simulation

class State:
	def __init__(self, name, actFunc=None, isAccept=False):
		self.name = name
		self.act = actFunc
		self.transTable = {}
		self.isAccept = isAccept

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

class FSM:
	def __init__(self, states, start, tokenList=None):
		self.states = states
		self.start = start
		self.tokenList = tokenList

	def setTokenList(self, tokenList):
		self.tokenList = tokenList

	def execute(self):
		print('FSM is start')
		now = self.start
		# if now.act:
			# now.act()
		for token in self.tokenList:
			print('get token %s' % token)
			if token in now.transTable:
				print('from %s to %s' % (now.name, now.transTable[token].name))
				now = now.transTable[token] # transform to next state
				if now.act: now.act() # state behavior
			else:
				print('this token %s is not in transTable' % token)
				# TODO: stop FSM, error end

		if now.isAcceptState():
			print('Accept')
		print('FSM is finish')


S1 = State('s1', isAccept=True)
S2 = State('s2')
S1.addTransform('1', S1)
S1.addTransform('0', S2)
S2.addTransform('1', S2)
S2.addTransform('0', S1)
states = [S1, S2]

print(S1)
print(S2)

fsm = FSM(states, S1, '101101000')
fsm.execute()

