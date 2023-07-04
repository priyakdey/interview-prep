def rotate(arr, n):
    print("inside before", id(arr))
    arr.insert(0, arr[-1])
    del arr[-1]


arr = [1, 2, 3, 4, 5]
print("outside before", id(arr))
rotate(arr, len(arr))
print("outside after", id(arr))
print(arr)
