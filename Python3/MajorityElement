from typing import List
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         # Hashmap approach.
#         #empty dict initialized to keep a track of the frequency of each element
#         count = {} 
#         res, maxCount =0,0 #res = number with maxCount

#         # now we should iterate through all of nums
#         for n in nums:
#             # adds 1 to existing count if it's already in dict
#             # or initializes to 1 if not in dict
#             # .get(n,0) returns 0 if n is not yer a key
#             count[n] = 1+ count.get(n,0)
#             res = n if count[n] > maxCount else res
#             maxCount = max(count[n], maxCount)
#         return res
#         # Time: O(n)- one pass through array of size n
#         # Space: O(n)- In worst case, we store n different numbers in dictionary.

# ------------------------- Boyer Moore Voting Algorithm--------------------

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0,0
        for n in nums:
            if count ==0:
                res =n
            if n == res:
                count += 1
            else:
                count= count-1 #count -=1
        return res 