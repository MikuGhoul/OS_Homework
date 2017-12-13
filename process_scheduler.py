import os
import time
import copy

ready_queue = []


class ProcessProto:
    def __init__(self, _arrive_time, _service_time, _priority, _obj_name):
        self.arrive_time = _arrive_time
        self.service_time = _service_time
        self.priority = _priority
        self.obj_name = _obj_name


# 先来先服务调度
def FCFS(_process_list, start_time, finish_time, turn_time, weight_turn_time, current_time):
    _process_list.sort(key = lambda x: x.arrive_time)

    while ready_queue:
        print (ready_queue[0].obj_name, end=' ')

        start_time.append(current_time)
        current_time += ready_queue[0].service_time
        finish_time.append(current_time)
        turn_time.append(current_time - ready_queue[0].arrive_time)
        weight_turn_time.append(float(format(((current_time - ready_queue[0].arrive_time) / ready_queue[0].service_time), '.2f')))
        
        _process_list.remove(ready_queue[0])
        del ready_queue[0]

        if _process_list:
            current_time = max(_process_list[0].arrive_time, current_time)
            ready_queue.append(_process_list[0])

    print ("\nstart time:" + str(start_time))
    print ("finish time:" + str(finish_time))
    print ("turnaround time:" + str(turn_time))
    print ("weighted turnaround time" + str(weight_turn_time))
    print ("average turnaround time:%0.2f" % (sum(turn_time) / int(len(turn_time))))
    print ("average weighted turnaround time:%0.2f" % (sum(weight_turn_time) / int(len(weight_turn_time))))

    

# 短作业优先调度
def SPN(_process_list, start_time, finish_time, turn_time, weight_turn_time, current_time):
    _process_list.sort(key = lambda x: x.service_time)
    while ready_queue:
        print (ready_queue[0].obj_name, end=' ')

        start_time.append(current_time)
        current_time += ready_queue[0].service_time
        finish_time.append(current_time)
        turn_time.append(current_time - ready_queue[0].arrive_time)
        weight_turn_time.append(float(format(((current_time - ready_queue[0].arrive_time) / ready_queue[0].service_time), '.2f')))
        
        _process_list.remove(ready_queue[0])
        del ready_queue[0]
        if _process_list:
            current_time = max(_process_list[0].arrive_time, current_time)
            ready_queue.append(_process_list[0])

    print ("\nstart time:" + str(start_time))
    print ("finish time:" + str(finish_time))
    print ("turnaround time:" + str(turn_time))
    print ("weighted turnaround time" + str(weight_turn_time))
    print ("average turnaround time:%0.2f" % (sum(turn_time) / int(len(turn_time))))
    print ("average weighted turnaround time:%0.2f" % (sum(weight_turn_time) / int(len(weight_turn_time))))


def Priority(_process_list, start_time, finish_time, turn_time, weight_turn_time, current_time):
    # _process_list.sort(key = lambda x: x.priority)
    _process_list.sort(key = lambda x: x.arrive_time)

    while ready_queue:
        print (ready_queue[0].obj_name, end=' ')

        start_time.append(current_time)

        # 找在当前进程的服务时间内到达且优先级比当前进程高的进程
        flag = False
        for p in _process_list:
            if p != ready_queue[0]:
                if p.arrive_time < ready_queue[0].service_time + current_time and p.priority < ready_queue[0].priority:
                    flag = True
                    break
        # 由于是抢占式，要切换进程，并保存上一个进程的PCB，这里指更新time
        if flag:
            current_time = p.arrive_time
            ready_queue[0].service_time -= current_time 
            ready_queue.insert(0, p)
            continue
            

        current_time += ready_queue[0].service_time
        finish_time.append(current_time)
        turn_time.append(current_time - ready_queue[0].arrive_time)
        weight_turn_time.append(float(format(((current_time - ready_queue[0].arrive_time) / ready_queue[0].service_time), '.2f')))
        
        _process_list.remove(ready_queue[0])
        del ready_queue[0]
        if _process_list:
            current_time = max(_process_list[0].arrive_time, current_time)
            if not ready_queue.count(_process_list[0]):
                ready_queue.append(_process_list[0])

    print ("\nstart time:" + str(start_time))
    print ("finish time:" + str(finish_time))
    print ("turnaround time:" + str(turn_time))
    print ("weighted turnaround time" + str(weight_turn_time))
    print ("average turnaround time:%0.2f" % (sum(turn_time) / int(len(turn_time))))
    print ("average weighted turnaround time:%0.2f" % (sum(weight_turn_time) / int(len(weight_turn_time))))
    

# 几个算法的calc time和print抽象出来
def do_scheduler(fun_list):
    global ready_queue
    for fun in fun_list:
        # 防止浅copy，就每次计算一遍了
        # （深copy时，del和remove的元素地址变了后居然找不到
        process_list = [A, B, C, D, E]

        # 最小到达时间的进程入等待队列
        _min_time = 1 << 30
        for p in process_list:
            if p.arrive_time <= _min_time:
                _min_time = p.arrive_time
                _min = p
        ready_queue.append(_min)

        start_time = []
        finish_time = []
        turn_time = []
        weight_turn_time = []
        current_time = ready_queue[0].arrive_time

        print (fun.__name__)
        fun(process_list, start_time, finish_time, turn_time, weight_turn_time, current_time)
        print ('\n')


if __name__ == '__main__':
    A = ProcessProto(0, 4, 2, 'A')
    B = ProcessProto(1, 3, 3, 'B')
    C = ProcessProto(2, 5, 1, 'C')
    D = ProcessProto(3, 2, 4, 'D')
    E = ProcessProto(4, 4, 0, 'E')    

    do_scheduler([FCFS, SPN, Priority])