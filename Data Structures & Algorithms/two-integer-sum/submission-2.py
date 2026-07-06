class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}

        for i,j in enumerate(nums):
            temp=target-j

            if temp in hashmap:
                return [hashmap[temp],i]
            hashmap[j]=i