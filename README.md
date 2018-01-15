# OS HOMEWORK

* [Banker algorithm](#banker-algorithm)

* [Process scheduling algorithm](#process-scheduling-algorithm) 

* [Thread synchronization](#thread-synchronization)

* [MMU](#mmu)

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

## MMU
``` python
[{0: 0}, {0: 1}, {0: 2}, {0: 3}, {0: 4}, {0: 5}, {0: 6}, {0: 7}, {0: 8}, {0: 9}, {0: 10}, {0: 11}, {0: 12}, {0: 13}, {0: 14}, {0: 15}, {0: 16}, {0: 17}, {0: 18}, {0: 19}, {1: 0}, {1: 1}, {1: 2}, {1: 3}, {1: 4}, {1: 5}, {1: 6}, {1: 7}, {1: 8}, {1: 9}, {1: 10}, {1: 11}, {1: 12}, {1: 13}, {1: 14}, {1: 15}, {1: 16}, {1: 17}, {1: 18}, {1: 19}, {2: 0}, {2: 1}, {2: 2}, {2: 3}, {2: 4}, {2: 5}, {2: 6}, {2: 7}, {2: 8}, {2: 9}, {2: 10}, {2: 11}, {2: 12}, {2: 13}, {2: 14}, {2: 15}, {2: 16}, {2: 17}, {2: 18}, {2: 19}, {3: 0}, {3: 1}, {3: 2}, {3: 3}, {3: 4}, {3: 5}, {3: 6}, {3: 7}, {3: 8}, {3: 9}, {3: 10}, {3: 11}, {3: 12}, {3: 13}, {3: 14}, {3: 15}, {3: 16}, {3: 17}, {3: 18}, {3: 19}, {4: 0}, {4: 1}, {4: 2}, {4: 3}, {4: 4}, {4: 5}, {4: 6}, {4: 7}, {4: 8}, {4: 9}, {4: 10}, {4: 11}, {4: 12}, {4: 13}, {4: 14}, {4: 15}, {4: 16}, {4: 17}, {4: 18}, {4: 19}, {5: 0}, {5: 1}, {5: 2}, {5: 3}, {5: 4}, {5: 5}, {5: 6}, {5: 7}, {5: 8}, {5: 9}, {5: 10}, {5: 11}, {5: 12}, {5: 13}, {5: 14}, {5: 15}, {5: 16}, {5: 17}, {5: 18}, {5: 19}, {6: 0}, {6: 1}, {6: 2}, {6: 3}, {6: 4}, {6: 5}, {6: 6}, {6: 7}, {6: 8}, {6: 9}, {6: 10}, {6: 11}, {6: 12}, {6: 13}, {6: 14}, {6: 15}, {6: 16}, {6: 17}, {6: 18}, {6: 19}, {7: 0}, {7: 1}, {7: 2}, {7: 3}, {7: 4}, {7: 5}, {7: 6}, {7: 7}, {7: 8}, {7: 9}, {7: 10}, {7: 11}, {7: 12}, {7: 13}, {7: 14}, {7: 15}, {7: 16}, {7: 17}, {7: 18}, {7: 19}, {8: 0}, {8: 1}, {8: 2}, {8: 3}, {8: 4}, {8: 5}, {8: 6}, {8: 7}, {8: 8}, {8: 9}, {8: 10}, {8: 11}, {8: 12}, {8: 13}, {8: 14}, {8: 15}, {8: 16}, {8: 17}, {8: 18}, {8: 19}, {9: 0}, {9: 1}, {9: 2}, {9: 3}, {9: 4}, {9: 5}, {9: 6}, {9: 7}, {9: 8}, {9: 9}, {9: 10}, {9: 11}, {9: 12}, {9: 13}, {9: 14}, {9: 15}, {9: 16}, {9: 17}, {9: 18}, {9: 19}]
[{0: 10}, {1: 11}, {2: 12}, {3: 13}, {4: 14}, {5: 15}, {6: 16}, {7: 17}, {8: 18}, {9: 19}]
[10, [{0: 10}, {1: 11}, {2: 12}, {3: 13}, {4: 14}, {5: 15}, {6: 16}, {7: 17}, {8: 18}, {9: 19}]]
Input the page number: 2
Input the page address: 19

physical memory:
        page number:12
        page address:19
```