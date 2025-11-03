def linearSearch(data_list, target):
    for i in range(len(data_list)):
        if data_list[i] == target:
            return i
    return -1

# 정렬되어 있지 않은 리스트
test_list = [5, 2, 8, 1, 9, 4]
target1 = 8
index1 = linearSearch(test_list, target1)
target2 = 10
index2 = linearSearch(test_list, target2)

print("[ Linear search ]")
print(f"target1: {target1}, index1: {index1}")
print(f"target2: {target2}, index2: {index2}")

# 실행은 터미널에 python3 search.py 입력하면 됨
# 또는 우상단의 ▷ 버튼
# target1: 8, index1: 2
# target2: 10, index2: -1


def binarySearch(data_list, target):
    low = 0
    high = len(data_list) - 1
    while low <= high:
        mid = (low + high) // 2

        if data_list[mid] == target:
            return mid
        elif data_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    # 반복문이 종료될 때까지 찾지 못하면 -1 을 반환
    return -1

# 정렬되어 있는 리스트
test_list = [1, 2, 5, 8, 10, 12]
target1 = 8
index1 = linearSearch(test_list, target1)
target2 = 13
index2 = linearSearch(test_list, target2)

print("\n [ Binary search ]")
print(f"target1: {target1}, index1: {index1}")
print(f"target2: {target2}, index2: {index2}")

# target1: 8, index1: 2
# target2: 10, index2: -1
# target1: 8, index1: 3
# target2: 13, index2: -1