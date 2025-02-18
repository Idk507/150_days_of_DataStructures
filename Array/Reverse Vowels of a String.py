"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = ['a','e','i','o','u','A','E','I','O','U']
        i = 0
        j = len(s)-1
        s = list(s)
        while(i<j):
            if s[i] not in vowel: 
                i+=1
            if s[j] not in vowel:  
                j-=1
            if s[i] in vowel and s[j] in vowel:
                s[i],s[j] = s[j],s[i]
                i+=1
                j-=1
        s = "".join(s)        
        return s    
