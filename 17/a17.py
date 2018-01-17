#!/usr/bin/env python

step = 354

arr = [0]
ptr = 0
stop = 2017 

for i in range(1,stop+1):
    ptr = (ptr + step)%len(arr) + 1
    arr.insert(ptr, i)

for i in range(len(arr)):
    if arr[i] == 2017:
        print(arr[(i+1)%len(arr)])
