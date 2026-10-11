class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        # b=0
        # for i in range(1,len(nums)+1):
        #     if len(nums)%i==0:
               
        #         b+=nums[i-1]**2

        # return b
        b=0
        for i,num in enumerate(nums,start=1):
            if len(nums)%i==0:
                b+=num**2

        return b