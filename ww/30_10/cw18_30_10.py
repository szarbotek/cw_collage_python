from random import randint

x = [1, 3, 1000, 8, 7]
x.sort()
print(x[0], x[-1])


def quicksort2(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[ arr.__len__() //2]
        
        left, middle, right = [], [], []
        for i in arr:
            if i < pivot:
                left.append(i)
            if i == pivot:
                middle.append(i)
            if i > pivot:
                right.append(i)
        
        return quicksort2(left) + middle + quicksort2(right)

# Example usage
array = [randint(0,1000_000) for _ in range(1_000_000) ]
sorted_array = quicksort2(array)
print(sorted_array)