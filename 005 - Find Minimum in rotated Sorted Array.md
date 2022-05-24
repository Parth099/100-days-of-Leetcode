| **Date**    | **Link**                                                                                | Difficulty |
| ----------- | --------------------------------------------------------------------------------------- | ---------- |
| May 24 2022 | [#153](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/submissions/) | *Easy*     |

# Find Minimum in rotated Sorted Array
## Optimal Solution

Type: **O**(`log n`)

```py
def findMin(self, nums):
    l, r = 0, len(nums) - 1
    while(l != r): #without convergence
        m = l + (r - l) / 2 #just to remember this for typed languages
        if nums[m] > nums[r]: 
            #middle element is bigger then end: the start of the array must be in nums[m+1:r]
            #the middle element is already larger than r so its not the smallest here
            l = m + 1
        else:
            r = m

    return nums[r]
```

This code is quite straight forward. The only explanation it needs is the `if` statement. 

If `nums[m] > nums[r]`, then the middle of the array has a larger element then the ending element. If this is true then we know that `nums[m]` **cannot** be the smallest element. Thus the smallest element **must be** in the indexes `[m+1, ..., r]`. 

If that was not the case the array is sorted in the index range `[m, ..., r]` and thus the smallest element will be in the index range `[l, ..., m]`. We cannot make any conclusions about `nums[m]` here. 

**Will the `while` loop always terminate**? The `if` statement deceases the index range *every* iteration.  