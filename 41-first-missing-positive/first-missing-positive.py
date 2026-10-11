class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        a=1
        nums.sort()

        for i in nums:
            if i==a and a>0:
                a+=1
            elif i>a:
                return a

        return a
