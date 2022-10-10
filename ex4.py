def string (rle):
    l = len(rle)
    p = rle[0]
    count = 1
    res = ""
    for i in range(l - 1):
        c = rle[i + 1]
        if (c == p):
            count += 1
        else:
            res += p + str(count)
            count = 1
        p = c
    res += p + str(count)
    return res
print(string( 'AVVVBBBVVXDHJFFFFDDDDDDHAAAAJJJDDSLSSSDDDD'))