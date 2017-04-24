
'''
import random


data = ['tara', 'basro', 'gones']
print len(data)
#print data.random()

print '-------------------'

for i in range(0, len(data)):
    random.shuffle(data)
    print data[0]
    del data[0]

mirdan = ['a', 'b', 'c', 'd']

print mirdan.pop(2)

print mirdan
print ''.join(mirdan)

print ' '.join(list(mirdan))
'''

from sys import exit

def gold_room():
    print "This room is full of gold. How much do you take?"
    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        print("Man, learn to type a number.")
    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        print("You greedy bastard!")
gold_room()
