#4 adalah 100 dalam biner dan 11 adalah 1011. Apa keluaran dari operator bitwise berikut?

a=4       #4=100
b=11     #11=1011


#a
print("soal 4|11")
c= a|b
print("Hasil a|b adalah : ", c)
print('nilai:',a,',binary:',format(a,'08b'))
print('nilai:',b,',binary:',format(b,'08b'))
print('nilai:',c,',binary:',format(c,'08b'))
print('-------------------------')

#b
print ('soal 4>>11')
c= a>>b
print("Hasil a>>b adalah : ", c)
print('nilai:',a,',binary:',format(a,'08b'))
print('nilai:',b,',binary:',format(b,'08b'))
print('nilai:',c,',binary:',format(c,'08b'))
print('-------------------------')

#c
print ('soal 4^11')
c=a^b
print("Hasil a^b adalah : ", c)
print('nilai:',a,',binary:',format(a,'08b'))
print('nilai:',b,',binary:',format(b,'08b'))
print('nilai:',c,',binary:',format(c,'08b'))
print('-------------------------')

#d
print ('soal ~4')
c=~a
print("Hasil ~a adalah : ",c )
print('nilai:',a,',binary:',format(~a,'08b'))

print('-------------------------')

#e
print ('soal 11 & 4')
c= b & a
print("Hasil b&a adalah : ",c)
print('nilai:',a,',binary:',format(a,'08b'))
print('nilai:',b,',binary:',format(b,'08b'))
print('nilai:',c,',binary:',format(c,'08b'))