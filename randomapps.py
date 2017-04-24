import random
'''
database = []
words_input1 = raw_input('Input Nama: ')
words_input2 = raw_input('Input Nama: ')


database.append(words_input1);
database.append(words_input2);

print database
'''
print 'Masukan nama yang akan anda random!'



def randomize_tool():

    for i in range(0, len(data)):
        random.shuffle(data)
        print (i+1) ,'.', data[0]
        del data[0]


var = 1
data = []
while var == 1:
    words_input =raw_input()
    if len(words_input) == 0:
        print 'This is the random result!'
        print '-----------------'
        randomize_tool()
        print '-----------------'
        print 'That it is...!'
        print 'Press Ctr-C to close the Program!'
    else:
        data.append(words_input);




'''
while (len(data[count]) > 0 ):
    data = []
    words_input = raw_input('Masukan Nama: ')
    data.append(words_input);
    print data
    count = count + 1
'''
