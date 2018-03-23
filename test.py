
'''
x= raw_input()
a = "They fools"
print a[0]

def b():
     c=[word for line in a for word in a.split()]
     print c[0]
b()


iput=raw_input()

iput = int(iput)

v = 3
a = iput + 3
print a



'''
'''
import re
s = '1208uds9f8sdf978qh39h9i#H(&#*H(&H97dgh'
s_ = filter(lambda c: c.isalpha(), s)
#print s_
l = ["pow ow","gee em"]
#l = list(range(10))
#l = list(map(lambda x:x.isalpha(), l))

#print l

l=re.split(' (?<=e)', l[1])
print l

name = 'Came@lCase.Test123'
splitted = re.sub('(?!^)(@)', r' ', name).split()
print splitted
re.split('(?<!\d)[,.]|[,.](?!\d)', splitted[1])

print splitted


line = 'path:bte00250 Alanine, aspartate and glutamate metabolism path:bte00330 Arginine and proline metabolism'
line =re.split(' (?=:)', line)
#print line

#l = list(range(10))
#l = list(map(lambda x:x*x, l))

#l = list(filter(lambda x: x > 10 and x < 80, l))
'''
import string

number_filter=  list(range(9))
letter_filter= list(string.ascii_lowercase) and list(string.ascii_lowercase)
dashscore_filter=['-','_']
all_filter = number_filter + letter_filter + dashscore_filter
#all_filter = ''.join(word[0] for word in all_filter)
l = ["Pow9ow=","gee em"]
print all_filter
#l = map(lambda x:x.isalpha(), l[0])
hasil =list(filter(lambda x: x == number_filter, l[0]))
#l = lambda l:l.isalpha()
#s = not(number_filter)
#if map(lambda l:l.isalpha()) and map(lambda l:l.is)

print l
print hasil

#print list(isalpha())
