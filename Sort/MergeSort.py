def merge(items, temp, low, mid, high):
    i = low
    j = mid + 1
    for k in range(low, high+1):
        if i > mid:
            # 왼쪽 리스트의 순회를 마쳤음
            # 남은 오른쪽 리스트의 원소들은 모두 왼쪽 리스트 원소보다 작음
            temp[k] = items[j]
            # 뒤에 나머지는 정렬되어있으니 그대로 넣기
            j += 1
        elif j > high:
            # 오른쪽 리스트의 순회를 마쳤음
            # 남은 왼쪽 리스트 원소들은 모두 오른쪽 리스트 원소보다 작음
            temp[k] = items[i]
            # 앞의 나머지는 정렬되어있으니 그대로 넣기
            i += 1
        elif items[j] < items[i]:
            # 왼쪽 리스트의 원소가 더 큰 경우
            # 오른쪽 리스트의 원소를 정렬리스트에 넣을거임
            temp[k] = items[j]
            j += 1
            # 오른쪽 리스트 다음 원소를 비교해보자
        else:
            # 왼쪽 리스트의 원소가 더 작거나 같은 경우
            # 왼쪽 리스트의 원소를 정렬리스트에 넣을거임
            temp[k] = items[i]
            i += 1
            # 왼쪽 리스트 다음 원소를 비교해라
    for k in range(low, high+1):
        items[k] = temp[k]
        # 이제 정렬해놓은거 원래 리스트로 복사해라

def merge_sort(items, temp, low, high):
    if high <= low:
        return None
    # 다 정렬했으면 이제 끝내라
    mid = low + (high - low)//2
    # low, high, mid 는 값이 아니라 index 값임
    merge_sort(items, temp, low, mid)
    merge_sort(items, temp, mid+1, high)
    merge(items, temp, low, mid, high)

if __name__ == '__main__':
    items = [5,4,3,3,5,6,4,4,3,2]
    temp = [None]*len(items)
    print('정렬 전 : \t', end ='')
    print(items)
    merge_sort(items, temp, 0, len(items)-1)
    print('정렬 전 : \t', end='')
    print(items)