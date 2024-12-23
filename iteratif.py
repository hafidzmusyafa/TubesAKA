def iteratifAlgo(arr, dest):
    for i in range(len(arr)):
        if arr[i] == dest:
            return i
    return -1