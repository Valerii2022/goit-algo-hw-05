def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return (iterations, arr[mid])
        elif arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1
    
    return (iterations, upper_bound)

# тест

sorted_arr = [0.1, 0.5, 1.3, 2.7, 3.6, 4.4, 5.8, 6.9]
target_value = 3.0

result = binary_search(sorted_arr, target_value)
print(result) 

sorted_arr_second = [0.1, 0.5, 1.3, 2.7, 3.6, 4.4, 5.8, 6.9, 7.6, 8.9, 9.4, 10.9, 11.7, 12.8, 13.3, 14.0]
target_value_second = 7.0

result = binary_search(sorted_arr_second, target_value_second)
print(result) 