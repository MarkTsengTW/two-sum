class Solution(object):
    def twoSum(self, nums, target):
        hashtable = {}
        for i in range(0, (len(nums))):
                hashtable[nums[i]] = i
        for i in range(0, (len(nums))):
            second_value = target - nums[i]
            try:
                if hashtable[second_value] is not i:
                    return i, hashtable[second_value]
            except KeyError:
                pass
