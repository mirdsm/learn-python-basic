
import random 

Keluarga = ['Andi','Ibu','Bapak','Kakak']
Umur = ['12','54','55','23']


input = raw_input('Masukan Umur\n')
g = "Tidak ada Anggota Keluarga yang umur segitu, coba lagi!"

def fgh(input):
	if input in Umur:
		s = Keluarga[Umur.index(input)]
		print 'Itu adalah umur dari ' + s + '!'
	else:
   		print g 
print fgh(input)