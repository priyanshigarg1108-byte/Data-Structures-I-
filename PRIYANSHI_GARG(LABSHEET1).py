#ques 1

# import time
#
# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1
#
# # Different array sizes
# sizes = [10000, 50000, 100000]
#
# target = -1  # Target not present (worst case)
#
# for n in sizes:
#     arr = list(range(n))
#
#     start = time.perf_counter()
#
#     result = linear_search(arr, target)
#
#     end = time.perf_counter()
#
#     # Convert seconds into microseconds
#     execution_time = (end - start) * 1_000_000
#
#     print("Array Size:", n)
#     print("Target Found At Index:", result)
#     print("Execution Time:", round(execution_time, 2), "microseconds")
#     print("---------------------------")

#ques2
import time
import math

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Sorted array
arr = list(range(10000))
target = 9999

start = time.time()
result = binary_search(arr, target)
end = time.time()

print("Target found at index:", result)
print("Execution time:", end - start)
print("Time Complexity: O(log n)")

#ques 3
import time

m = 5
n = 5

start = time.time()

print("Nested loop time complexity analysis:")

for i in range(m):
    for j in range(n):
        print("*", end=" ")
    print()

end = time.time()

print("Execution time:", end - start)
print("Time Complexity: O(m*n)")



















#