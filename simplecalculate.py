F= (1,2,3,4)


'''
Tahap:
1. masukan ke values list
2. masukan satu persatu angka ke function
3. Isi function: kali setiap angka antara satu dengan yang lain, lalu bagi dengan angka yang dimasukan
4. masukan lagi ke list variabel baru
5. print list. 
'''
#a = []
def input_data():
	a = []
	input = raw_input()
	for i in range(0,input)
		b = raw_input()
		a.insert(0,b)
	return a


def func_three():
	for i in range(1,len(a)):
		a.remove(a[i])    
	return a 

#result1 = int(A[0]) * int(A[1]) * int(A[2]) * int(A[3])
#print result1
#c = []
def func_two():
	
	#for i in range(0,4):
   #	a = [1,2,3,4]	
	#for i in range(1,len(a)):
	#	c = []
	#	a.remove(a[i])                #      [2,3,4]

		#for i in range(0,len(a)):         
	z = a[i]                       # [2]
	a.remove(a[i])
	for i in range(1,len(a)):   
		z = z * a[i]
	c.insert(0,z)
    print c

func_two()



			#c.insert(0,result2)
	
print c[::-1]

