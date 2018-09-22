

from multiprocessing import JoinableQueue,Process

def customer (queue) :
    while True:
        r = queue.get()
        print("消费:" + r)
        queue.task_done() # 消费完成, 通知继续生产


def product(queue,name) :
    for i in range(10):
        queue.put(name)
        print("生产骨头")
        queue.join() # 阻塞当前,让队列中其他执行

if __name__ == '__main__':
    queue = JoinableQueue()
    cus = Process(target=customer,args=(queue,))
    cus.daemon = True # 设置开启之前, 一旦进程开启了, 设置不好使
    pro = Process(target=product,args=(queue,"骨头"))
    cus.start()
    pro.start()
    print("e")
