# OS HOMEWORK

* [Banker algorithm](#banker-algorithm)

* [Process scheduling algorithm](#process-scheduling-algorithm) 

* [Thread synchronization](#thread-synchronization)

## Banker algorithm
``` python
P0/P1/P2/P3/P4
Choose a thread: (Example: 4)
1

Input a request list: (Example: 1, 4, 7)
1 0 2
Option 1: 13024

Option 2: 13042

Option 3: 13204

Option 4: 13240

Option 5: 13402

Option 6: 13420

Option 7: 14302

Option 8: 14320
```
## Process scheduling algorithm
``` python
FCFS
A B C D E
start time:[0, 4, 7, 12, 14]
finish time:[4, 7, 12, 14, 18]
turnaround time:[4, 6, 10, 11, 14]
weighted turnaround time[1.0, 2.0, 2.0, 5.5, 3.5]
average turnaround time:9.00
average weighted turnaround time:2.80


SPN
A D B E C
start time:[0, 4, 6, 9, 13]
finish time:[4, 6, 9, 13, 18]
turnaround time:[4, 3, 8, 9, 16]
weighted turnaround time[1.0, 1.5, 2.67, 2.25, 3.2]
average turnaround time:8.00
average weighted turnaround time:2.12


Priority
A C E C A B D
start time:[0, 2, 4, 8, 9, 11, 14]
finish time:[8, 9, 11, 14, 16]
turnaround time:[4, 7, 11, 13, 13]
weighted turnaround time[1.0, 7.0, 5.5, 4.33, 6.5]
average turnaround time:9.60
average weighted turnaround time:4.87


RR
A B C D E A B C D E A B C E A C E C
start time:[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
finish time:[9, 12, 15, 17, 18]
turnaround time:[6, 11, 15, 13, 16]
weighted turnaround time[3.0, 3.67, 3.75, 3.25, 3.2]
average turnaround time:12.20
average weighted turnaround time:3.37
```
## Thread synchronization
``` python
Enter the number of producers:4
Enter the number of consumers:3
producing:Thread-1[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
producing:Thread-2[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
producing:Thread-3[1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
producing:Thread-4[1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
consuming:Thread-5[0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
consuming:Thread-6[0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
consuming:Thread-7[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
producing:Thread-1[1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
consuming:Thread-5[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
producing:Thread-2[1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
producing:Thread-4[1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
producing:Thread-3[1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
...
```