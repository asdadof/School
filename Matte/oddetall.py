def oddetall(n):
    L = [1, 3, 5, 7]
    x = []

    for i in range(4,0,-1):
        j = 0
        while n > 4**i:
            n -= 4**i
            j += 1
        
        x.append(L[j])

    if n != 0:
        x.append(L[n-1])
    return x
print(oddetall(642))