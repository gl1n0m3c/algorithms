def binary_search(list, item):
    low = 0
    hight = len(list) - 1

    while low <= hight:
        mid = (low + hight) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess == item:
            hight = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3))
print(binary_search(my_list, -1))



# Задачка с leetcode на бинарный поиск https://leetcode.com/problems/search-in-rotated-sorted-array/description/ (medium)
def BinSearch(nums, target):
    left = 0
    right = len(nums) - 1
    print(left, right)
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        else:
            if nums[mid] >= nums[left]:  # перехода не было
                if nums[left] <= target < nums[mid] :
                    right = mid - 1
                else:
                    left = mid + 1
            else:                        # переход был
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        print(left, right)
        print()
    return -1  # число не найдено
