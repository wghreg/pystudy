#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from multiprocessing import Process, Queue
import os, time, random

def write(q):
    print("Process to write: %s"%os.getpid())
    for value in ["A", "B", "C"]:
        print("Put %s to queue..."% value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    print("Process to read: %s"% os.getpid())
    while True:
        value = q.get(True)
        print("Get %s from queue."% value)

if __name__ == "__main__":
    q = Queue()     # 父进程创建Queue，并传给各个子进程：
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()      # 启动子进程pw，写入:
    pr.start()      # 启动子进程pr，读取:
    pw.join()       # 等待pw结束:
    pr.terminate()  # pr进程里是死循环，无法等待其结束，只能强行终止: