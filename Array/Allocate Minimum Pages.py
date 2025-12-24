class Solution:
    def findPages(self, arr, k):
        
        # code here
        n = len(arr)
        if k > n :
            return -1
        def possible(arr,n,k,mid):
            student = 1
            page = 0
            for i in range(n):
                if arr[i] > mid : return False
                if page + arr[i] > mid :
                    student +=1 
                    page = arr[i]
                    if student  > k :
                        return False
                else :
                    page += arr[i]
            return True
        
        high = max(arr)
        arrsum = sum(arr)
        result = -1
        while high <= arrsum :
            mid = (high + arrsum) // 2
            
            if possible(arr, n, k , mid):
                result = mid
                arrsum = mid - 1
            else :
                high = mid + 1
        return result
                
                
                
        
        
        
