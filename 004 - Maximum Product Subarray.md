| **Date**    | **Link**                                                        | Difficulty |
| ----------- | --------------------------------------------------------------- | ---------- |
| May 23 2022 | [#152](https://leetcode.com/problems/maximum-product-subarray/) | *Medium*   |

# Maximum Product Subarray
## Optimal Solution

Type: **O**(n)

```py
def maxProduct(self, nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	currMax, currMin, globalMax = nums[0], nums[0], nums[0] 
	# at the first index; first number is max and min
	for i in range(1, len(nums)):
		x, y = currMax * nums[i], currMin * nums[i] 
		#stored so they only need to be calc-ed once
		localMax = max(x, y, nums[i]) 
		localMin = min(x, y, nums[i])

		currMax, currMin = localMax, localMin
		globalMax = max(localMax, globalMax)

	return globalMax
```

Start off by assume the first element is the largest and the smallest.
For each other number we attain the max result, by the end we should have the largest contiguous product.

Notice there are three ways to get the largest Product Subarray at an index `i`. 

+ The moving product is currently negative and thus any positive number will be the *new* max.
+ The moving product is currently negative and thus any negative number times the moving product will be new largest product
+ The moving product is already positive and any positive number will continue the chain 

Intermediate variables are **required** since we don't want one of the max/min to effect each other while we are changing them.

This is a problem where solving sub-problems is the key. At each point we must know the min/max attainable so far. Realize this, if there are no `0`s in the array each number **will effect** the min/max. If there is a 0 we will need to restart the count.

**How is 0 being handled here**?
If a `0` occurs it *will* make each max/min equal to 0. However for the next iteration it will also be zero and thus the next numbers that show up and *refill* the data.