#stack1 is non-classified version

STKSIZE=3
ptr= -1

def push(stk,x):
	global ptr
	global STKSIZE
	if ptr<STKSIZE-1:
		ptr+=1
		stk[ptr]=x
		return stk
	else:
		print('stack overflow')

def pop(stk):
	global ptr
	if ptr>-1:
		s=stk[ptr]
		ptr-=1
		return s
	else:
		print('stack empty')

stack1=[None]*STKSIZE
push(stack1,1)
push(stack1,2)
push(stack1,3)
push(stack1,4)
print(pop(stack1))
print(pop(stack1))
print(pop(stack1))
print(pop(stack1))

#stack2 is classified version

class Stack:
	def __init__(self,size=3):
		self.ptr=-1
		self.size=size
		self.stk=[None]*size

	def isEmpty(self):
		return self.ptr == -1 # ptr<0

	def isFull(self):
		return self.ptr == self.size-1 #ptr>size-2

	def push(self,x):
		if self.isFull():
			print('stack overflow')
		else:
			self.ptr+=1
			self.stk[self.ptr]=x
			return self

	def pop(self):
		if self.isEmpty():
			print('stack empty')
		else:
			s=self.stk[self.ptr]
			self.ptr-=1
			return s

stack2=Stack(3)
stack2.push(1)
stack2.push(2)
stack2.push(3)
stack2.push(4)
print(stack2.pop())
print(stack2.pop())
print(stack2.pop())
print(stack2.pop())

