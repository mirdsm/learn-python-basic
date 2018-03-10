

def input_data():
	a = []
	inp = int(raw_input())
	for i in range(0,inp):
		b = int(raw_input())
		a.append(b)
	
	#print a
	return a
	
def min_list(a):
	#a = [1,2,3]

	c = []
	temp = a
	for i in range(0,len(a)):
		#a = [1,2,3]
		print "--------------"
		print "this is i", i
		print "This is Temp", temp
		a.remove(a[i]) 
		print "This is Temp asbis remove", temp
		print "this is a after remove", a
		sum = 1
		for item in a:
			print "This is item", item
			print "This is list of a", a
			sum = sum * item
			print "This is sum", sum
		print "Temp sebelum loop", temp
		a = temp
		c.append(sum)
		#print c
	#printc
	return 

#input_data()
a = input_data()
min_list(a)

