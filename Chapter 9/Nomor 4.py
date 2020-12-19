import random
import sys
def shuffleString (kata, n):
    listhasil = []
    i = 0
    while (len(listhasil) < n):   
        hasil = ''.join(random.sample(kata, len(kata)))
        if hasil not in listhasil :
            listhasil += [hasil]
            i += 1
    print (listhasil)
    
shuffleString('aku', 2)
shuffleString('aku', 3)
shuffleString('aku', 4)
