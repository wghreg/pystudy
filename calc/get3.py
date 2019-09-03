#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time

def isPrime(num):
    for i in range(2, (int)(num/2)):
        if num % i ==0:
            return False
        return True

def getThreeNumbers(num):
    res = 0
    for i in range(3, num, 2):
        n = i
        while(n>0):
            if n%10 == 3:
                res = res +1
            n = int(n/10)
    print('3 出现的次数：'+ res)

def getWechatID(num):
    for i in range(2, int(num/2)):
        if num % i !=0:
            continue
        div = int(num /i)
        if not isPrime(i) or not isPrime(div):
            continue

        res = ''
        if div > i:
            res = res + str(div) + str(i)
        else:
            res = res + str(i) + str(div)
        getThreeNumbers(int(res))
        print('微信ID: NY'+ res)
        return

start = time.time()
getWechatID(707829217)
end = time.time()
print("Time cost : "+ str(end - start))
