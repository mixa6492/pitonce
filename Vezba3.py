import sys
import math

n = [8,10,16,4,5,21,11,7,1,3]
print("Uneti niz je: \n", n)

def maxHeapify(A, i, heapSize):
    l = 2*i + 1
    r = 2*i + 2
    if(l <= heapSize and A[l]> A[i]):
        largest = l 
    else:
        largest = i

    if(r <= heapSize and A[r] > A[largest]):
        largest = r

    if (largest != i):
        temp = A[i]
        A[i] = A[largest]
        A[largest] = temp

        
#A[i],A[largest] = A[largest],A[i] -- mala pomoc   
        maxHeapify(A, largest, heapSize)
        

def buildMaxHeap(A, heapSize):
    i = 1
    for i in range(int(math.floor(len(A)/2))-1, -1, -1):
        maxHeapify(A, i, heapSize)

def heapSort(A, heapSize):
    buildMaxHeap(A, heapSize)
    for i in range(len(A)-1, 0, -1):
        A[0],A[i] = A[i],A[0]
        #temp = A[0]
        #A[0] = A[i]
        #A[i] = temp
        heapSize = heapSize - 1
        maxHeapify(A, 0, heapSize)

def heapMax(A):
    return A[1]

def heapExtractMax(A, heapSize):
    if (heapSize < 0):
        print("Heap Underflow")
        return

    max = A[0]
    temp = A[heapSize]
    A.remove(A[heapSize])
    A[0] = temp
    heapSize = heapSize - 1
    maxHeapify(A, 0, heapSize)
    return max

def maxHeapInsert(A, key, heapSize):
    heapSize = heapSize + 1
    #A = -math.inf
    #A.insert(heapSize, key)
    A.append(-(sys.maxsize)) #-- ovo je za beskonacno
    heapIncreaseKey(A, heapSize, key)

def heapIncreaseKey(A, i, key):
    if(key < A[i]):
        print("New key is smaller than current key")

    A[i] = key
    while(i > 1 and A[math.floor((i - 1)/2)] < A[i]):
        A[i],A[math.floor((i - 1)/2)] = A[math.floor((i - 1)/2)],A[i]
        i = math.floor((i - 1)/2)


heapSize = len(n)-1
buildMaxHeap(n, heapSize)
print("Posle Build Max Heap: \n", n)

heapSort(n, heapSize)
print("Posle Heap Sort: \n", n)

#heapExtractMax(n, heapSize)
#print("Posle Heap Extract Max: \n", n)

maxHeapInsert(n, 5, heapSize)
print("Posle Max Heap Insert: \n", n)

