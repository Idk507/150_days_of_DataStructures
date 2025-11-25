def subarray_sum(arr, n, s):
    start = 0
    curr_sum = 0
    
    for end in range(n):
        curr_sum += arr[end]
        
        # Shrink window if sum exceeds target
        while curr_sum > s and start < end:
            curr_sum -= arr[start]
            start += 1
        
        # Check if we found the sum
        if curr_sum == s:
            return [start + 1, end + 1]  # 1-based indexing
    
    return [-1]
