import sys

_ANS_THREAD = []
_FINISH = []
MAX = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
Allocation = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]
Available = [3, 3, 2]
Need = []
Work = []
_sum = 0
source_num = 0

# map每个MAX/Allocation的list，再map每个list，用lambda优化
def calc_need(_max1, _allocation1):
    return list(map(lambda _max2, _allocation2:_max2 - _allocation2, _max1, _allocation1 ))

def dfs(runned_thread, all_thread, first_thread):
    global _ANS_THREAD, _FINISH, Allocation, Available, Need, Work, _sum
    if runned_thread == all_thread:
        _sum += 1
        print ("Option " + str(_sum) + ": ",end='')
        for _ans in _ANS_THREAD:
            print (_ans, end='')
        print ('\n')
        return
    temp_thread = 0
    while (temp_thread != all_thread):
        if _FINISH[temp_thread]:
            temp_thread += 1
            continue
        # print (temp_thread)
        flag = True

        temp_source = 0
        while (temp_source != source_num):
            if Need[temp_thread][temp_source] > Work[temp_source]:
                flag = False
                break
            temp_source += 1
        if not flag:
            temp_thread += 1
            continue

        # 找到一个满足自身need和finish的线程，更新 Work
        temp_source = 0
        while (temp_source != source_num): 
            Work[temp_source] += Allocation[temp_thread][temp_source]
            temp_source += 1
        _FINISH[temp_thread] = True
        _ANS_THREAD.append(temp_thread)

        dfs(runned_thread + 1, all_thread, first_thread)

        # dfs数据回溯
        _ANS_THREAD.pop()
        temp_source = 0
        while (temp_source != source_num):
            Work[temp_source] -= Allocation[temp_thread][temp_source]
            temp_source += 1
        _FINISH[temp_thread] = False
        temp_thread += 1

if __name__ == '__main__':
    # global _ANS_THREAD, _FINISH, Allocation, Available, Need, Work, source_num
    # calc Need
    Need = list(map(calc_need,MAX,Allocation))

    # input thread and request list
    thread = int(input("P0/P1/P2/P3/P4\nChoose a thread: (Example: 4)\n"))
    Request = input("\nInput a request list: (Example: 1, 4, 7)\n").split(' ')
    Request = list(map(lambda _req : int(_req), Request))

    # banker_algorithm
    ## step 1
    for i, j in zip(Request, Need[thread]):
        if i > j:
            print ("Request Error. Request source num >= Need source num")
            sys.exit(0)

    ## step 2
    for i, j in zip(Request, Available):
        if i > j:
            print ("Request Waiting. Request source num >= Available source num.")
            sys.exit(0)
    
    ## step 3
    source_num = len(Available)
    temp_source = 0
    while (temp_source != source_num):
        Available[temp_source] -= Request[temp_source]
        Allocation[thread][temp_source] += Request[temp_source]
        Need[thread][temp_source] += Request[temp_source]
        temp_source += 1
    
    ## step 4
    Work = Available
    temp_thread_num = 0
    while (temp_thread_num != len(MAX)):
        _FINISH.append(False)
        temp_thread_num += 1
    _ANS_THREAD.append(thread)
    _FINISH[thread] = True
    temp_source = 0
    while (temp_source != source_num):
        Work[temp_source] += Allocation[thread][temp_source]
        temp_source += 1
    dfs(1, len(MAX), thread)
