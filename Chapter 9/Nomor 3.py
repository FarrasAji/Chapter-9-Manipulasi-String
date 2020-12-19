def bintang(n):
    i = 0
    j = 1

    while i < n/2 :        
        star = '*' * j
        i += 1
        j += 2
        print (star.center(10))
        
    j -= 2

    while i >= n/2 :
        j -= 2
        i += 1
        star = '*' * j
        print (star.center(10))
        if i == n :
            break
bintang (7)
