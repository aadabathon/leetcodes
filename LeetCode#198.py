#[nums], find largest non-contiguous sum.
#for the ith house, max(dp[i-1], dp[i-2] + nums[i])
#could achieve o(1) space complexity with two variables.


class Solution(object):
        def rob(self,nums):
                dp = [0] * len(nums)
                if len(nums) == 0:
                        return 0
                elif len(nums) == 1:
                        return nums[0]
                elif len(nums) ==2:
                        return max(nums[0],nums[1])
                else:
                        dp[0] = nums[0]
                        dp[1] = max(nums[0], nums[1])
                for i in range(2, len(nums)):
                        dp[i] = max(dp[i-1], dp[i-2] + nums[i])

                return dp[len(dp)-1]
                
