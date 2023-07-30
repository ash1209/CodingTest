
# 문제 링크 : https://leetcode.com/problems/find-anagram-mappings/description/?envType=study-plan-v2&envId=premium-algo-100

class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = list()
        num_dict = {}
        
        for idx, num in enumerate(nums2):
            num_dict[num] = idx
        
        for num in nums1:
            l.append(num_dict[num])

        return l
        
