
# Aplikasi sederhana dari deret fibonacci


input_number = int(raw_input('Masukan angka untuk menentukan seberapa panjang deret ini? '))
var1 = 0
var2 = 1
print var1
print var2
for i in range(0, input_number):
    var3 = var2 + var1
    print var3
    var1 = var2
    var2 = var3
