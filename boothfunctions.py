#Booths Functions (Add, RightShift)

def add(bNum1, bNum2):
	result=[0]*17
	carry=0
	i=16

	while i>=0:
		temp=bNum1[i]+bNum2[i]+carry
		result[i]=temp%2
		carry=temp/2
		i-=1
	return result

def RightShift(bNum):
	i=16
	while i>=1:
		bNum[i]=bNum[i-1]
		i-=1
	return bNum