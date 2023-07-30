# 문제 : https://leetcode.com/problems/max-consecutive-ones-ii/?envType=study-plan-v2&envId=premium-algo-100

# 0과 1로 이루어진 list가 주어졌을 때, 단 하나의 0만 1로 치환할 수 있다. 이 때 연속된 1의 개수가 최대인 경우는 몇 인지를 구해야 하는 문제

# 0인 애들의 인덱스를 담는 list 생성 후, 이 list[n] - list[n-1] 이런 식으로 풀면 될 것 같은데, 일단 틀림 ㅎㅎㅎ
# 코드의 문제인지, 접근 방법에서 고려하지 않은 부분이 있는지 확인해봐야 겠다.
# 일단은 오늘은 여름 휴가를 다녀와서 너무 피곤해서 머리가 너무 멍한 상태라,,, 내일 다시 맑은 정신으로 풀어봐야겠다.

class Solution:
   def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_num = 0
        zlist = []

        for idx, num in enumerate(nums):
            if num == 0:
                zlist.append(idx) 

        if len(zlist) <= 1:
            return len(nums)
        elif len(zlist) == 2:
            return max(zlist[-1], (len(zlist) - (zlist[0]+1)) )
        else:
            max_num = zidx[1]
            for idx, zidx in enumerate(zlist[1:-1]):
                if idx == 0:
                    max_num = max(max_num, zidx - zlist[idx-1])
            max_num = max(max_num, len(nums) - (zlist[-2]+1))
        
        return max_num
