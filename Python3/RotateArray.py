# problem 189. 
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # Using new empty array then copying back to nums
        # uses extra memory
        n = len(nums) #Basic arithmetic O(1)
        k= k % n #in case given k exceeds nums length  #Basic arithmetic O(1)

        # creates a list of size n. So takes O(n) time
        tempNums= [0]*n 
        for i in range(n): # again runs for size of n so takes O(n) time
            newIndex= (i+k)%n  #Basic arithmetic O(1)
            tempNums[newIndex] = nums[i]  #Basic arithmetic O(1)
            #overall the above for loop takes O(n) time
        #copy back to nums and return
        for i in range(n): #again for n iterations so O(n) time
            nums[i] = tempNums[i]
#Therefore final total time takes O(n)+O(n)+O(n)= O(n)
# Space complexity: Only one data structure list used of size n so O(n)
"""
## ----------------- Reverse method (Inplace manipulation --------------
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums) #if k exceeds nums length
        #reverse nums
        nums.reverse() #O(n) time

        # reverse first k elements
        nums[:k]= reversed(nums[:k]) #O(k) time
        # reverse the rest of nums i.e. n-k elements
        nums[k:] = reversed(nums[k:]) #O(n-k)

# Time complexity= O(n)+O(k)+O(n-k)= O(n)
# space complexity = O(1) as all operations are done in-place no extra data structures used.
"""

#------------- Cyclic Replacements (in-place manipulation)----------

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n= len(nums)
        k= k%n #in case k exceeds nums length
        count =0 #tracks manipulated elements in the array
        start=0 # the algorithm should start at index 0

        while count < n:
            current= start #current index we are working with
            prev= nums[start]
            while True:
                destIndex= (current+ k)%n
                nums[destIndex], prev= prev, nums[destIndex]
                current= destIndex
                count+=1
                if start == current:
                    break
            start += 1
# Time = O(n) Even though it looks like nested loops, each element is moved exactly once, so time is still linear.
# Space= O(1)






        






        """
        Do not return anything, modify nums in-place instead.
        """
      
        
