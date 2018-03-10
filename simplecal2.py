A = [1,2,3,4]

result1 = int(A[0]) * int(A[1]) * int(A[2]) * int(A[3])
#print result1
list = []
for i in range(0,4):	
	result2 = result1/int(A[i])
	list.insert(0,result2)
print A	
print list[::-1]

