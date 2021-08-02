"""
Membuat program untuk menghitung jumlah kura-kura setalah 
365 hari.
"""
j_kura2 = 9999 #Jumlah awal kura-kura
h_lahir = 90 #Setiap 90 hari setiap 1 kura-kura melahirkan 1 anak
j_mati = 21.1/100 #Sebelum melahirkan 21,1% kura-kura meninggal

hari = 365
j_melahirkan = int(hari/90) #berapa kali kura2 akan melahirkan selama 365 hari
for i in range(j_melahirkan):
    j_kura2 = j_kura2*j_mati*2
    
print("Jumlah kura-kura setelah 365 hari: {}".format(int(j_kura2)))




