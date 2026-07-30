class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[]
        
        prefix=1
        suf=1
        n=len(nums)
        suffix=[1]*n
        for i in range(n):
            if i!=0:
                prefix=prefix*nums[i-1]
            result.append(prefix)
        for i in range(n-1,-1,-1):
            suffix[i]=suf
            suf*=nums[i]

        for i in range(n):
            result[i]*=suffix[i]
        return result
            




