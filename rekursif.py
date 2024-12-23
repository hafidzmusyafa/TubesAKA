def rekursif_sequential_search(arr, dest,  i = 0):
    if i >= len(arr):
        return -1
    if arr[i] == dest:
        return i
    return rekursif_sequential_search(arr, dest, i = i + 1)

