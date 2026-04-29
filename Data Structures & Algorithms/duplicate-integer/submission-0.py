class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create a dict
        d = {}
        # iterate through nums
        for i in range(len(nums)):
            # check if there is a current entry of the integer in the dictionairy
            if nums[i] in d:
                # if yes return True
                return True
            # if not we added the entry to our dictionary, note that -1 is just a filler value.
            d[nums[i]] = -1 
        return False