def bintang(n):
    i = 0
    j = 1
    while i < n :
        star = '*' * (1 + (i-1)*2)
        i+=1
        j+=2
        print (star.center(10))
bintang (5)
