def find_max(arr):
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num

arr = [10, 3, 45, 67, 2, 99, 23]
print("Maximum number is:", find_max(arr))