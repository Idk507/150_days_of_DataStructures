class Solution:
    def isBalanced(self, s):
        # code here
        val = {"()","[]","{}"}
        open ="([{"
        stack = []
        for i in s:
            if i in open :
                stack.append(i)
            else :
                if not stack or stack.pop() + i not in val :
                    return False
        return not stack
                
        
        
