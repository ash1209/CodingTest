# 문제 : https://leetcode.com/problems/palindrome-permutation/description/?envType=study-plan-v2&envId=premium-algo-100

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        bit_map = 0b0
        odd = 0

        for c in s:
            bit_map = bit_map ^ (1<<(ord(c) - ord('a'))) 

        for i in range(0, 26):
            if bit_map & (1 << i):
                odd += 1 

        return odd < 2
