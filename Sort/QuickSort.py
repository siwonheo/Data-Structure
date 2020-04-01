def partition(items, pivot, high):
    i = pivot + 1
    j = high
    while True:
        while i < high and items[i] < items[pivot]:
            i += 1
            # 피벗보다 큰 원소를 찾을 때까지 오른쪽으로 이동
            # 끝까지 가면 종료
        while j > pivot and items[j] > items[pivot]:
            j -= 1
            # 피벗보다 작은 원소를 찾을 떄까지 왼쪽으로 이동
            # 끝까지 가면 종료
        if j <= i:
            #j랑 i 위치 역전되면 종료
            break
        items[i], items[j] = items[j], items[i]
        # i가 더 작으면 i번째랑 j번쨰 원소 바꿈
        i += 1
        j -= 1
    items[pivot], items[j] = items[j], items[pivot]
    # i와 j 위치 바뀌면 피벗이랑 j 위치 바꿈
    return j
    #피벗이 j로 바뀜

def quick_sort(items, low, high):
    if low < high:
        pivot = partition(items, low, high)
        quick_sort(items, low, pivot-1)
        quick_sort(items, pivot+1, high)

if __name__ == '__main__':
    items = [54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 11, 31, 22, 44, 17, 20]
    print('변경 전 : \t', end='')
    print(items)
    quick_sort(items, 0, len(items)-1)
    print('변경 후 : \t', end='')
    print(items)

"""
54  88  26  93  17  49  10  17  77  11  31  22  44  17  20
 p   i                                                   j
54  20  26  93  17  49  10  17  77  11  31  22  44  17  88
 p       i                                           j
54  20  26  93  17  49  10  17  77  11  31  22  44  17  88
 p           i                                       j
54  20  26  17  17  49  10  17  77  11  31  22  44  93  88
 p           i                                       j
54  20  26  17  17  49  10  17  77  11  31  22  44  93  88
 p               i                               j    
54  20  26  17  17  49  10  17  77  11  31  22  44  93  88
 p                               i               j 
54  20  26  17  17  49  10  17  44  11  31  22  77  93  88
 p                               i               j 
54  20  26  17  17  49  10  17  44  11  31  22  77  93  88
 p                                   i       j  
54  20  26  17  17  49  10  17  44  11  31  22  77  93  88
 p                                           j   i
break
22  20  26  17  17  49  10  17  44  11  31  54  77  93  88
                                           pivot
                                           
return 11
"""