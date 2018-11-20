# traffic light simulation
from time import sleep


class Counter:
	def __init__(self):
		self.n = 0
	
	def tick(self):
		self.n += 1
		return self.n
	
	def reset(self):
		self.n = 0
	
	def getNumber(self):
		return self.n

transferTable = {}
transferTable['Red'] = {'wait':5, 'next':'Green'}
transferTable['Green'] = {'wait':10, 'next':'Yellow'}
transferTable['Yellow'] = {'wait':1, 'next':'Red'}

# initialization
c = Counter()
state = 'Green'
while True:
	print('State: %s t=%ds' % (state, c.getNumber()))
	# check time of waiting
	if c.getNumber() >= transferTable[state]['wait']:
		print('turn to next state(%s)' % transferTable[state]['next'])
		c.reset()
		state = transferTable[state]['next']
	
	# tick, simulation for time pass
	sleep(1)
	c.tick()
