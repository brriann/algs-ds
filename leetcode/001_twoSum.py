class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return self.twoSumONLogN(nums, target)
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
    def twoSumONLogN(self, nums, target):
        eltIdxMap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in eltIdxMap:
                return [eltIdxMap[complement], i]
            # no match found - so add current elt:idx to map
            eltIdxMap[nums[i]] = i

sol = Solution()
print(sol.twoSum([1,2,3], 5))

