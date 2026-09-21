class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # l=list(set(nums))
        # l.sort()
        # c=0
        # for i in range(1,len(l)):
        #     if l[i]-l[i-1]==1:
        #         c=c+1
        #     # else:
        #     #     c=0
        # return c+1

        ns=set(nums)
        longest=0

        for i in ns:
            if i-1 not in ns:
                l=1

                while i+l in ns:
                    l=l+1
                longest=max(longest,l)
        return longest

                