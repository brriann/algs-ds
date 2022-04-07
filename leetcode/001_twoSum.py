class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return self.twoSumONSquared(nums, target)
    def twoSumONSquared(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        def twoSumON(self, nums, target):
            # TODO
# client
sol = Solution()
var = sol.twoSum([1,2,3], 4)
print(var)
