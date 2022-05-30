| **Date**    | **Link**                                                             | Difficulty |
| ----------- | -------------------------------------------------------------------- | ---------- |
| May 29 2022 | [#167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | *Medium*   | 

# Two Sum - Sorted Array
## Optimal Solution

Type: **O**(n)

```py
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start, end = 0, len(nums) - 1
        pointerSum = None
        while start < end:
            
            pointerSum = nums[start] + nums[end]
            
            if  pointerSum == target:
                return [start + 1, end + 1]
            
            elif pointerSum > target:
                end -= 1
            else:
                start += 1
                
        return [] #not possible to get here in this problem
```

Reading the code is enough to understand whats going on here. 

