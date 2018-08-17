board=[[' ' for i in range(10)] for j in range(10)]

def isEmpty(x):
	return x == ' '

def isSame(x1,x2):
	return x1 == x2

def getNext(brd,x,y,vx,vy):
	if (x+vx) != -1 and (x+vx) != 10 and (y+vy) != -1 and (y+vy) != 10:
		return brd[x+vx][y+vy]
	else:
		return ' '

def getLen(brd,x,y,vx,vy):
	len=0
	if !isEmpty(brd[x][y]):
		while isSame(brd[x][y],getNext(brd,x,y,vx,vy)):
			len+=1
			x+=vx
			y+=vy
	return len

def getFullLen(brd,x,y):
	direct=[[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,-1],[-1,1],[1,-1]] # 8 direction
	lens=[]
	for i in range(1,7,2):
		len1=getLen(brd,x,y,direct[i][0],direct[i][1])
		len2=getLen(brd,x,y,direct[i+1][0],direct[i+1][1])
		lens.append(len1+len2+1)
	return lens

def has5stone(lens):
	for l in lens:
		if l==5:
			return True
	return False

def move(brd,x,y,clr):
	if isEmpty(brd[x][y]):
		brd[x][y]=clr
		return True
	else:
		return False

def showLine(brd,x):
	s=''+str(x)
	for i in brd[x]:
		s+=i
	print(s)

def show(brd):
	print("_0123456789")
	for x in range(10):
		showLine(brd,x)

