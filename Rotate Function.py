class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n=len(nums)
        total_sum=sum(nums)
        current_sum=sum(i*nums[i] for i in range (n))
        ans=current_sum
        for i in range (1,n) :
            current_sum += total_sum-n*nums[n-i]
            ans=max(ans,current_sum)
        return ans
