def isUpperCaseLetter(c):
	return c>='A' and c<='Z'

def isNumber(c):
	return c>='0' and c<='9'

def checkRest(s):
	for i in range(2,9): #3~9 in real
		if not isNumber(s[i]):
			return False
	return True

def checkID(s):
	county={'A':'10','B':'11','C':'12','D':'13','E':'14','F':'15','G':'16','H':'17','I':'34','J':'18','K':'19',
'L':'20','M':'21','N':'22','O':'35','P':'23','Q':'24','R':'25','S':'26','T':'27','U':'28','V':'29','W':'32','X':'30','Y':'31','Z':'33'}
	w=[1,9,8,7,6,5,4,3,2,1,1]

	#check len
	if len(s)!=10:
		print('len != 10')
		return False
	#check County
	elif not isUpperCaseLetter(s[0]):
		print('county code is wrong')
		return False
	#check F/M
	elif s[1]!='1' and s[1]!='2':
		print('F/M error')
		return False
	#check Rest char
	elif not checkRest(s):
		print('has non-number code in rest')
		return False
	else:
		print('in last part: check sum')
		s=s.replace(s[0],county[s[0]])
		checkSum=0
		for i in range(len(s)):
			x=int(s[i])
			checkSum+=x*w[i]
			print('i=%d, x=%d, w=%d, x*w=%d sum=%d' % (i,x,w[i],x*w[i],checkSum))
		return checkSum%10==0

pat='^([A-Z]{1})([1-2]{1}\d{8})$'
import re
def checkID2(s):
	county={'A':'10','B':'11','C':'12','D':'13','E':'14','F':'15','G':'16','H':'17','I':'34','J':'18','K':'19',
'L':'20','M':'21','N':'22','O':'35','P':'23','Q':'24','R':'25','S':'26','T':'27','U':'28','V':'29','W':'32','X':'30','Y':'31','Z':'33'}
	w=[1,9,8,7,6,5,4,3,2,1,1]
	pattern=re.compile(pat)
	match=pattern.match(s)
	if match:
		s=county[match.group(1)]+match.group(2)
		checkSum=0
		for i in range(len(s)):
			x=int(s[i])
			checkSum+=x*w[i]
			print('i=%d, x=%d, w=%d, x*w=%d sum=%d' % (i,x,w[i],x*w[i],checkSum))
		return checkSum%10==0
	else:
		return False
