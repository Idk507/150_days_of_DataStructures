"""
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxl = 0
        cs = set()
        l,r =0,0
        while r< n:
            if s[r] not in cs:
                cs.add(s[r])
                maxl = max(maxl,r-l+1)
                print(maxl)
            else:
                while s[r] in cs:
                    if s[l] in cs:
                        cs.remove(s[l])
                    l+=1
                    print(l)
                cs.add(s[r])
            r+=1
        return maxl



        
