# 문제 : https://leetcode.com/problems/palindrome-permutation/description/?envType=study-plan-v2&envId=premium-algo-100

# 문자열이 주어졌을 때, 문자를 재배치 해서 회문이 될 수 있는지를 판별하는 문제
# Hash를 쓰면 너무 쉽게 풀리지만, 그건 너무 쉬워서 Hash 말고 다른 더 재미있는 방법이 없을까 고민하다가
# Bit Masking을 사용해서도 풀 수 있지 않을까 해서 풀어본 문제


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
