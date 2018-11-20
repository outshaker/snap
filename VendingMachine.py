# Vending machine simulation
from time import sleep
from random import random, choice


class Machine:
	priceList = {'A':10, 'B':15, 'C':20}
	def __init__(self, items=None, deposit=50):
		self.income = 0
		self.items = items or {'A':5, 'B':5, 'C':5}
		self.deposit = deposit

	def insertCoin(self, n):
		print('insert coin %d' % n)
		self.income += n
		return 'loadCoin'

	def _refund(self):
		if self.income:
			print('return coin %d' % self.income)
			self.income = 0
			# send back coin TODO: API call

	def cancel(self):
		print('cancel')
		self._refund()
		return 'ready'

	def _buyItem(self, name):
		if self.items[name] > 0 and self.income >= self.priceList[name]:
			print('send a goods: %s' % name)
			self.items[name] -= 1
			self.income -= self.priceList[name]
			# TODO: Need to confirm if there is enough balance
			self._refund()
			return 0 # success
		elif self.income < self.priceList[name]:
			print('Insufficient amount, needs %d coin(s)' % (self.priceList[name]-self.income))
			return 1 # Insufficient amount
		elif self.items[name] <= 0:
			print('item %s is sold out' % name)
			return 2 # sold out
		else:
			print('something wrong, back to state<insertCoin>')
			return -1

	def buyItem(self, name):
		respond = self._buyItem(name)
		if respond == 0:
			return 'ready'
		else:
			return 'loadCoin'


def randwalk(state):
	cmdTable = {}
	cmdTable['ready'] = ['insertCoin', 'cancel']
	cmdTable['loadCoin'] = ['insertCoin', 'cancel', 'buyItem']
	coinList = [1, 5, 10, 50]
	itemList = ['A', 'B', 'C'] # other way: get machine.items at runtime

	cmd = choice(cmdTable[state])
	if cmd == 'insertCoin':
		return cmd, choice(coinList)
	elif cmd == 'buyItem':
		return cmd, choice(itemList)
	else:
		return cmd

m = Machine()
s = 'ready'
cmd = ''
while True:
	print('state=%s' % s)
	cmd = randwalk(s)
	if type(cmd) is tuple:
		print('cmd=%s' % cmd[0])
		s = getattr(m, cmd[0])(cmd[1]) # call m.cmd(arg) & get next state
	else:
		print('cmd=%s' % cmd)
		s = getattr(m, cmd)()
	sleep(1)
