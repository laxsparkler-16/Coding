class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        
        if len(nums)>1 and  nums[0]==0 and nums[1]!=0:
            a=nums[0]
            nums[0]=nums[1]
            nums[1]=a
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==0 and nums[j]!=0:
                    a=nums[i]
                    nums[i]=nums[j]
                    nums[j]=a
                    

        