def trappingWater(arr, n):
    # Your code here
    left_max = arr[0]
    right_max = arr[n - 1]
    lo = 1
    high = n - 2
    result = 0
    while (lo <= high):
        if (left_max < right_max):
            if (arr[lo] >= left_max):
                left_max = arr[lo]
            else:
                result += left_max - arr[lo]
            lo += 1
        else:
            if arr[high] >= right_max:
                right_max = arr[high]
            else:
                result += right_max - arr[high]
            high -= 1

    return result

lis1 = [3,0,0,2,0,4]
lis2 = [8,8,2,4,5,5,1]

print(trappingWater(lis1, len(lis1)))
print(trappingWater(lis2, len(lis2)))
