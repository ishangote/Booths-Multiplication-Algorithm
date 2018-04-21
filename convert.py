#Conversion Functions

def convertToBinary(dNum):
	bNum=[0]*8					#bNum is a list! [0,0,0,...]
	i=7
	while dNum and i>=0:
		bNum[i]=dNum%2
		dNum/=2
		i-=1
	return bNum

def convertToDecimal(bNum):		#bNum is a list! [0,0,0,...]
	bLen=len(bNum)
	dNum=0
	for i in range(1, bLen+1):
		dNum=dNum+int(bNum[i-1])*2**(bLen-i)
	return dNum