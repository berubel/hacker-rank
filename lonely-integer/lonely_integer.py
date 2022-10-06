def lonelyinteger(a):
    
    for i in a:
        c = a.count(i)
        if c == 1:
            return i

if __name__ == '__main__':
    arr = [1,1,5,6,7,9,8,6,7,8,9]

    print(lonelyinteger(arr))