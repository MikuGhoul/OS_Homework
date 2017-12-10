import threading
import time

# 缓冲区
buffers = []
for i in range(20):
    buffers.append(0)

_wait_queue = {}

class Semaphore:
    def __init__(self, sem):
        self._sem = sem
        # self.lock = threading.Lock()
    def P(self):
        global _wait_queue
        self._sem -= 1
        if self._sem < 0:
            # block当前线程并加入等待队列
            _lock = threading.Lock()
            _wait_queue[threading.current_thread()] = _lock
            #print ('locking')
            _lock.acquire()
            _lock.acquire()
            #print ('locked')
            
    def V(self):
        self._sem += 1
        if self._sem <= 0:
            # 从等待队列中随机取出一个block线程并唤醒
            locked_thread = _wait_queue.popitem()
            #print ('wakeuping')
            locked_thread[1].release()
            #print ('wakeup done')



class BoundedBuffer:
    def __init__(self):
        # 互斥
        self.mutex = Semaphore(1)
        # 缓冲区不空
        self.fullBuffers = Semaphore(0)
        # 缓冲区不满
        self.emptyBuffers = Semaphore(20)
    def producer(self):
        while (True):
            global buffers
            self.emptyBuffers.P()
            self.mutex.P()
            # 生产
            for index in range(len(buffers)):
                if buffers[index] == 0:
                    buffers[index] = 1
                    break
            print ("producing:" + threading.current_thread().name + str(buffers))
            self.mutex.V()
            self.fullBuffers.V()
            time.sleep(1)

    def consumer(self):
        while (True):
            global buffers
            self.fullBuffers.P()
            self.mutex.P()
            # 消费
            for index in range(len(buffers)):
                if buffers[index] == 1:
                    buffers[index] = 0
                    break
            print ("consuming:" + threading.current_thread().name + str(buffers))
            self.mutex.V()
            self.emptyBuffers.V()
            time.sleep(1)
    
if __name__ == '__main__':
    bf = BoundedBuffer()
    producer_container = [threading.Thread(target = bf.producer) for i in range(4)]
    consumer_container = [threading.Thread(target = bf.consumer) for i in range(2)]

    for _thread in producer_container + consumer_container:
        _thread.start()
