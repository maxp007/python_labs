

def find_min(arr):
    min_val = arr[0]
    for i in arr:
        if min_val > i:
           min_val = i
    return min_val

def find_avg(arr):
    sum = 0
    for i in arr:
        sum = sum + i

    return sum/len(arr)

arr1 = [1,0,3,-1,4,7,5,1,-1,12,4,-8,8,-9,-2,4]
print(find_min(arr1))
print(find_avg(arr1))

arr3 = [1,6,3,-11,4,7,4,1,-8,11,0,-8,9,-9,-3,8]
print(find_min(arr3))
print(find_avg(arr3))