class Solution:
    def  towerOfHanoi(self, n, fromm, to, aux):
        # if n == 1 : 
        #     return 
        # self.towerOfHanoi(n-1,fromm,aux,to)
        # self.towerOfHanoi(n-1,aux,to,fromm)
        return 2**n-1
