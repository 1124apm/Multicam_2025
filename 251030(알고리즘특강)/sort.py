def selectionSort(data_list, descending=False):
    n = len(data_list)

    for i in range(n -1):
        target_index = i
        for j in range(i + 1, n):
            # 내림차순
            if descending:
                if data_list[j] > data_list[target_index]:
                    target_index = j
            # 오름차순
            else:
                if data_list[j] < data_list[target_index]:
                    target_index = j
            
            # 자리 바꾸기
            # 옛날 방식
            tmp = data_list[i]
            data_list[i] = data_list[target_index]
            data_list[target_index] = tmp

        return data_list

test_list = [5, 2, 8, 1, 9, 4]
result1 = selectionSort(test_list)
print(result1)  # [1, 2, 8, 5, 9, 4]
result2 = selectionSort(test_list, descending=True)
print(result2)  # [5, 1, 2, 8, 9, 4]


def bubbleSort(data_list, descending=False):
    n = len(data_list)

    # 1. Outer Loop: 정렬 과정을 n-1번 반복
    # 매 반복마다 가장 큰 요소가 제 위치(배열의 끝)로 '버블링'
    for i in range( n - 1 ):
        # 인접한 요소 비교
        if descending:
            if data_list[j] < data_list[j + 1]:
                data_list[j], data_list[j + 1] = data_list[j + 1], data_list[j]
                swapped = True
        else:
            if data_list[j] > data_list[j + 1]:
                data_list[j], data_list[j + 1] = data_list[j + 1], data_list[j]
                swapped = True
    
        # 3. 최적화: Inner Loop에서 한 번도 교환이 일어나지 않았다면,
        # 리스트는 이미 정렬된 상태이므로 반복을 종료
        if not swapped:
            break

# Insertion Sort, Quick Sort도 있음