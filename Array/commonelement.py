#User function Template for python3

class Solution:
    def commonElements(self, arr1, arr2, arr3):
        #Code Here
        return sorted(list(set(arr1) & set(arr2) & set(arr3)))
