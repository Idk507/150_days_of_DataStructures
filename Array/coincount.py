class Solution:
    def count(self, coins, sum):
        # code here 
        res = [0] * (sum+1)
        res[0] = 1
        for coin in coins :
            for i in range(coin,sum+1):
                # print(i)
                res[i] += res[i - coin]
                # print(res)
        # print(res)
        return res[sum]
