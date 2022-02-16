# Solution 1 - Kadanes Algorithm


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maximum_sum = current_sum = nums[0];
        
        for num in range(1,len(nums)):
            
            maximum_sum = max(nums[num],maximum_sum+nums[num]);
            
            if(maximum_sum > current_sum):
                
                current_sum = maximum_sum;
                
            
        return current_sum
        
        
        #solution 2
       
       
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maximum_sum=float('-inf')
        current_sum=0
        
        for num in nums:
            current_sum=max(num,current_sum+num);
            maximum_sum=max(maximum_sum,current_sum);
        return maximum_sum
