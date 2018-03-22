#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random, time, queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

task_queue = queue.Queue()      # 发送任务的队列
result_queue = queue.Queue()    # 接收结果的队列

class QueueManager(BaseManager):
    pass

# windows下运行
def return_task_queue():
    global task_queue
    return task_queue   # 返回发送任务队列
def return_result_queue():
    global result_queue
    return result_queue # 返回接收结果队列

def test():
    # QueueManager.register("get_task_queue", callable=lambda:task_queue)
    # QueueManager.register("get_result_queue", callable=lambda:result_queue)

    QueueManager.register("get_task_queue", callable=return_task_queue)
    QueueManager.register("get_result_queue", callable=return_result_queue)

    server_addr = '127.0.0.1'
    # windows需要写ip地址
    manager = QueueManager(address=(server_addr, 5000), authkey=b"abc")   # 绑定端口5000, 设置验证码'abc':
    manager.start()     # 启动Queue:
    # 获得通过网络访问的Queue对象:
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    '''
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    # 注意，当我们在一台机器上写多进程程序时，创建的Queue可以直接拿来用，
    # 但是在分布式多进程环境下，添加任务到Queue不可以直接对原始的task_queue进行操作，那样就绕过了QueueManager的封装，
    # 必须通过manager.get_task_queue()获得的Queue接口添加。
    '''
    # 放几个任务进去:
    for i in range(10):
        n = random.randint(0, 10000)
        print("Put task %d"% n)
        task.put(n)
    # 从result队列读取结果:
    print("Try get results...")
    for i in range(10):
        try:
            r = result.get(timeout=10)
            print("Result: %s"% r)
        except queue.Empty:
            print('result queue is empty.')

    manager.shutdown()      # 关闭
    print("master exit.")

if __name__ == "__main__":
    freeze_support()
    print("Start!")
    test()