def selection_sort(items):
    for i in range(0, len(items)-1):
        minimum = i
        for j in range(i, len(items)):
            if items[minimum] > items[j]:
                minimum = j
        items[i], items[minimum] = items[minimum], items[i]

def insertion_sort(items):
    for i in range(1, len(items)):
        for j in range(i, 0, -1):
            if items[j-1] > items[j]:
                items[j], items[j-1] = items[j-1], items[j]

def shell_sort(items):
    h = len(items)//2
    while h >= 1:
        for i in range(h, len(items)):
            j = i
            while j >= h and items[j] < items[j-h]:
                items[j], items[j-h] = items[j-h], items[j]
                j -= h
        print("{}-Sorted: ".format(h), items)
        h //= 2

def downheap(i, size):
    while 2*i + 1 <= size:
        k = 2*i+1
        if k < size - 1 and items[k] < items[k+1]:
            k += 1
        if items[i] >= items[k]:
            break
        items[i], items[k] = items[k], items[i]
        i = k

def heapify(items):
    hsize = len(items)
    for i in range(hsize//2 - 1, -1, -1):
        downheap(i, hsize)

def heap_sort(items):
    N = len(items)
    for i in range(N):
        items[0], items[N-1] = items[N-1], items[0]
        downheap(0, N-2)
        N -= 1


items = [39, 23, 15, 47, 11, 56, 61, 16, 12, 19, 21, 41]
print('before : ', end = '')
print(items)
heapify(items)
print('maxheap : ', end = '')
print(items)
heap_sort(items)
print('after : ',end = '')
print(items)