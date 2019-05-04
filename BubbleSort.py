import time as time
import numpy as np

def random_array(n):
    array = [] 
    for i in range(0, n, 1): 
        array.append(np.random.randint(0, 100))
    return array

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

global bubble_avg
bubble_avg = []
num_runs= 10
results = []

for r in range (num_runs):
        start_time = time.time()
        alist = random_array(100)
        bubbleSort(alist)
        end_time = time.time()
        time_elapsed = end_time - start_time
        results.append(time_elapsed)
        
a = sum(results)
average = (a/num_runs)
bubble_avg.append(average)

for r in range (num_runs):
        start_time = time.time()
        alist = random_array(250)
        bubbleSort(alist)
        end_time = time.time()
        time_elapsed = end_time - start_time
        results.append(time_elapsed)
        
a = sum(results)
average = (a/num_runs)
bubble_avg.append(average)

for r in range (num_runs):
        start_time = time.time()
        alist = random_array(500)
        bubbleSort(alist)
        end_time = time.time()
        time_elapsed = end_time - start_time
        results.append(time_elapsed)
        
a = sum(results)
average = (a/num_runs)
bubble_avg.append(average)

for r in range (num_runs):
        start_time = time.time()
        alist = random_array(750)
        bubbleSort(alist)
        end_time = time.time()
        time_elapsed = end_time - start_time
        results.append(time_elapsed)
        
a = sum(results)
average = (a/num_runs)
bubble_avg.append(average)

for r in range (num_runs):
        start_time = time.time()
        alist = random_array(1000)
        bubbleSort(alist)
        end_time = time.time()
        time_elapsed = end_time - start_time
        results.append(time_elapsed)
        
a = sum(results)
average = (a/num_runs)
bubble_avg.append(average)

for r in range (num_runs):
        start_time = time.time()
        alist = random_array(1250)
        bubbleSort(alist)
        end_time = time.time()
        time_elapsed = end_time - start_time
        results.append(time_elapsed)
        
a = sum(results)
average = (a/num_runs)
bubble_avg.append(average)

for r in range (num_runs):
        start_time = time.time()
        alist = random_array(2500)
        bubbleSort(alist)
        end_time = time.time()
        time_elapsed = end_time - start_time
        results.append(time_elapsed)
        
a = sum(results)
average = (a/num_runs)
bubble_avg.append(average)

for r in range (num_runs):
        start_time = time.time()
        alist = random_array(3750)
        bubbleSort(alist)
        end_time = time.time()
        time_elapsed = end_time - start_time
        results.append(time_elapsed)
        
a = sum(results)
average = (a/num_runs)
bubble_avg.append(average)

for r in range (num_runs):
        start_time = time.time()
        alist = random_array(5000)
        bubbleSort(alist)
        end_time = time.time()
        time_elapsed = end_time - start_time
        results.append(time_elapsed)
        
a = sum(results)
average = (a/num_runs)
bubble_avg.append(average)

for r in range (num_runs):
        start_time = time.time()
        alist = random_array(6250)
        bubbleSort(alist)
        end_time = time.time()
        time_elapsed = end_time - start_time
        results.append(time_elapsed)
        
a = sum(results)
average = (a/num_runs)
bubble_avg.append(average)

for r in range (num_runs):
        start_time = time.time()
        alist = random_array(7500)
        bubbleSort(alist)
        end_time = time.time()
        time_elapsed = end_time - start_time
        results.append(time_elapsed)
        
a = sum(results)
average = (a/num_runs)
bubble_avg.append(average)

for r in range (num_runs):
        start_time = time.time()
        alist = random_array(8750)
        bubbleSort(alist)
        end_time = time.time()
        time_elapsed = end_time - start_time
        results.append(time_elapsed)
        
a = sum(results)
average = (a/num_runs)
bubble_avg.append(average)

for r in range (num_runs):
        start_time = time.time()
        alist = random_array(10000)
        bubbleSort(alist)
        end_time = time.time()
        time_elapsed = end_time - start_time
        results.append(time_elapsed)
        
a = sum(results)
average = (a/num_runs)
bubble_avg.append(average)

print(bubble_avg)



























































































   