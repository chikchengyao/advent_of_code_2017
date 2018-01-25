#!/usr/bin/env python

step = 354
stop = 50000000

arr = {}
arr[0] = 0
ptr = 0

#def next(n):
#    if n == 0:
#        return ptr
#    else:
#        ptr = arr[ptr]
#        return next(n-1)

def pd(d, index):
    print(index, end=" ")
    if d[index] == 0:
        print()
        return
    else:
        pd(d, d[index])

for i in range(1,stop+1):
    if i%100000 == 0:
        print(i)
    for j in range(0,step):
        ptr = arr[ptr]
    arr[ptr], arr[i] = i, arr[ptr]
    ptr = arr[ptr]

print(arr[0])

