| **Date**    | **Link**                                                               | Difficulty |
| ----------- | ---------------------------------------------------------------------- | --------- |
| May 17 2022 | [#53](https://leetcode.com/problems/maximum-subarray/) | *Easy*    | 

# Maximum Subarray
## Optimal Solution
Type: **O**(n)

```py
def maxSubArray(self, nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	globalMax = localMax = float('-inf')
	for number in nums:
		localMax = max(number, localMax + number) #(A)
		globalMax = max(localMax, globalMax)

	return globalMax
```

At each `number` there are two decisions.
1. Add it to the moving array
2.	start the new array there

*Case 2* occurs when array is negative and a larger number (maybe negative) shows up.
 
This is handled by `(A)`. 

A separate variable is used to remember the *global* maximum.