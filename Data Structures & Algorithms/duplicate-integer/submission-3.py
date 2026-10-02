class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #hashset length method

        return len(set(nums)) < len(nums)