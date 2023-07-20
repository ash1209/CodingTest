'''
Given a string s, return the length of the longest substring that contains at most two distinct characters.

==================================================================
Example1 
Input: s = "eceba"
Output: 3
Explanation: The substring is "ece" which its length is 3.

Example2 
Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5.
==================================================================
'''

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        max_len = 0
        b, m, e = 0, 0, 0
        wq = [s[0]]

        if len(s) <= 2:
            return len(s)

        for i in range(1, len(s)):
            if len(wq) < 2 and s[i] != wq[0]:
                    wq.append(s[i])
                    m = i
            else: 
                if s[i] in wq: 
                    if s[i] != s[i-1]:
                        m = i
                else:
                    max_len = max(max_len, i - b)
                    if s[i-1] == wq[0]:
                        wq.pop(1)
                    else:
                        wq.pop(0)
                    
                    wq.append(s[i])
                    
                    b, m = m, i
            e = i 

        return max(max_len, e - b + 1)
