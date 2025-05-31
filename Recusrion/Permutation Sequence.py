"""
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

 

Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
Example 3:

Input: n = 3, k = 1
Output: "123"
 

Constraints:

1 <= n <= 9
1 <= k <= n!
"""
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def fact(n):
            if n == 0 : return 1 
            return fact(n-1)*n

        def getseq(n,k):
            seq = []
            k = k-1 
            for i in range(n-1,0,-1):
                q,r = k// fact(i) , k% fact(i)
                seq.append(q)
                k = r 
            return seq 

        sequence = getseq(n,k)
        res = ''
        arr = [str(i) for i in range(1,n+1)]
        while sequence : 
            ind = sequence.pop(0)
            res += arr[ind]
            del arr[ind]
        res += arr[0]
        return res
