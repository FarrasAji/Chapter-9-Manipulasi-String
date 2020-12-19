def ubahHuruf(teks, a, b) :
    daftarTeks = list(teks)

    akhir = ''    
    for karakterteks in daftarTeks :
        if(karakterteks == a):
            karakterteks = b
        akhir = ''.join([akhir,karakterteks])
    return akhir

print(ubahHuruf('MATEMATIKA', 'T', 'S'))
