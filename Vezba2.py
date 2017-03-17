import sys
import time
import random
import math

#el = [3,2,5,6,7,4,8,1]


#PRVI zadatak
def random_list (min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

def provera(A):
    y = list()
    y = A[:]
    y.sort()    

    for i in range(0, len(A)):
        if A[i] != y[i]:
            print(i)
            print(A)
            print(y)
            print("Nije dobro!")
        else:
            print("Ok.")


def insertionsort(A):
    for j  in range(2, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key


l = random_list(1, 100, 50)   
print("List: \n",l)

start_time = time.clock()

insertionsort(l)

end_time = time.clock() - start_time
print("Sortirano: \n",l)
#provera(l)
print("Duration insertionsort: ", end_time)


#DRUGI zadatak
t = random_list(1, 100, 50)
print("Nova lista: \n", t)

def mergesort(A, p, r):
    if p < r:
        q = math.floor((p + r)/2)
        mergesort(A, p, q)
        mergesort(A, q + 1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q 
    L = list()
    R = list()
    for i in range(0, n1):
        L.append(A[p + i - 1])
    for j in range(0, n2):
        R.append(A[q + j])

    L.append(sys.maxsize)
    R.append(sys.maxsize)

    i = 0
    j = 0

    for k in range(p, r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
     

start_time = time.clock()
mergesort(t, 0, len(t)-1)
end_time = time.clock() - start_time

print("Posle merge sorta: \n",t)

print("Duration merge sort: ",end_time)

#TRECI zadatak
def lineSearch(A, B):
    for i in range(0, len(A)):
        if A[i] == B:
            return i

print("Linearna pretraga: \n",lineSearch(l, 10))

#CETVRTI zadatak
def binarySearch(A, C):
    #mid = (len(A))//2
    #if len(A) == 0:
     #   raise "Error"
    #if C == A[mid]:
     #   return mid
    #elif C > A[mid]:
     #   return mid + binarySearch(A[mid:], C)
    #elif C < A[mid]:
     #   return binarySearch(A[mid:], C)
    #else:
     #   raise "Error"

    lower = 0
    upper = len(A)
    while lower < upper:
        x = lower + (upper - lower) // 2
        val = A[x]
        if C == val:
            return x
        elif C > val:
            if lower == x:
                break
            lower = x
        elif C < val:
            upper = x

b = random_list(1, 100, 50)
b.sort()

print("Binarna pretraga: \n",binarySearch(b, 20))