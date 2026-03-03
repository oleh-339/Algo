def counting_sort(arr):
    if not arr:
        return []

    n = len(arr)
    maxval = max(arr)
    counting_arr = [0] * (maxval + 1)

    for v in arr:
        counting_arr[v] += 1

    for i in range(1, maxval + 1):
        counting_arr[i] += counting_arr[i - 1]

    result = [0] * n

    for i in range(n - 1, -1, -1):
        v = arr[i]
        result[counting_arr[v] - 1] = v
        counting_arr[v] -= 1

    return result

def place(stiylo, c, dist, n):
    count = 1
    last = stiylo[0]
    
    for i in range(1, n):
        if stiylo[i] - last >= dist:
            count += 1
            last = stiylo[i]
            if count == c:
                return True
    return False

def find_distance(n, c, sections):
    stiylo = counting_sort(sections)
    
    low = 1
    high = stiylo[-1] - stiylo[0]
    result = 0
    
    while low <= high:
        mid = (low + high) // 2
        
        if place(stiylo, c, mid, n):
            result = mid
            low = mid + 13
        else:
            high = mid - 1
            
    return result