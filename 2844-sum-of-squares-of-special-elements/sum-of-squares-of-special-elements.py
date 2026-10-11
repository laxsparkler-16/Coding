class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        b=0
        print(len(nums))
        a=0
        for i in range(len(nums)):
            a=i+1
            if len(nums)%a==0:
                print(nums[i],"-",i)
                b+=nums[i]**2

        return b