import sys
import random
import matplotlib.pyplot as plt
import time

def Partition(A,p,r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i],A[j] = A[j],A[i]
    A[i + 1],A[r] = A[r],A[i + 1]
    return i + 1

def RandomizedPartition(A,p,r):
    i = random.randint(p,r)
    A[r],A[i] = A[i],A[r]
    return Partition(A,p,r)

def RandomizedQuicksort(A,p,r):
    if p < r:
        q = RandomizedPartition(A,p,r)
        RandomizedQuicksort(A,p,q - 1)
        RandomizedQuicksort(A,q + 1,r)

def QuickSort(A,p,r):
    if p < r:
        q = Partition(A,p,r)
        QuickSort(A, p, q - 1)
        QuickSort(A, q + 1, r)

def BucketSort(A):
    n = len(A)
    B = [None]*(n)
    for i in range(0, n):
        B[i] = list()
    for i in range(0, n):
        B[int(n*A[i])].append(A[i])
    for i in range(0, n):
        InsertionSort(B[i])
    return list(itertools.chain(*B))

def CountingSort(A,B,k):
    C = [None]*(k + 1)
    for i in range(0, k+1):
        C[i] = 0
    for j in rnage(1, len(A)):
        C[A[j]] = C[A[j]] + 1
    for i in range(1, k+1):
        C[i] = C[i] + C[i - 1]
    for j in range(len(A)-1, -1, -1):
        B[C[A[j]]] = A[j]
        C[A[j]] = C[A[j]] - 1

b = [10,8,4,1,7,6,9,5,3,2]

#Partition(n,0,len(n)-1)

#print("Posle Partiton Sort:\n ", n)

QuickSort(b, 0, len(b)-1)
print("Posle Quick Sort:\n ", b)

def random_list (min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

def CreatePlot(input_data, exec_time, algo_name):
    fig = plt.figure()     
    fig.suptitle(algo_name, fontsize=14, fontweight='bold')    
 
    ax = fig.add_subplot(111)
    fig.subplots_adjust(top=0.85)       
    ax.set_title('Vreme izvrsenja')
    ax.set_xlabel('Ulaz [n]')    
    ax.set_ylabel('Vreme [ms]')

    ax.plot(input_data, exec_time, '-', color='green')
    
    print(algo_name)
    for i in range(0, len(input_data)):
        print("input_data: ", input_data[i], ", exec_time: ", exec_time[i])

    return fig

def FirstPlot():
    # Measure exeuction time
    algo_name = "[FirstPlot] Quick Sort"
    input_data = []
    exec_time = []
    for n in range(100, 1100, 100):
        b = random_list(1,10000,n)
        start_time = time.clock() # expressed in seconds
        QuickSort(b,0,len(b)-1)
        end_time = time.clock()
        exec_time.append((end_time - start_time)*1000) #get miliseconds
        input_data.append(n)
    
    CreatePlot(input_data, exec_time, algo_name)

def ShowPlot():
    plt.show()

FirstPlot()

ShowPlot()