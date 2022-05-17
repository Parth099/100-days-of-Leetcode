| **Date**    | **Link**                                                            | Difficulty |
| ----------- | ------------------------------------------------------------------- | --------- |
| May 16 2022 | [#238](https://leetcode.com/problems/product-of-array-except-self/) | Medium          |

# Product of Array Except Self

Important constraint: 
```
'nums' (an array) to have 2 <= size <= 100000
```

## Optimal Solution

Type: **O**(n)

```py
def productExceptSelf(self, nums):
	"""
	:type nums: List[int]
	:rtype: List[int]
	"""
	copy = nums[:] #copy array
	n = len(nums)

	#Left process
	product = nums[0] #not all arrays start with '1'
	copy[0] = 1 #left product is empty and thus is '1'
	for x in range(1, n):
		copy[x] = product
		product *= nums[x]

	#right process
	product = nums[-1]
	for x in range(n - 2, -1, -1): #end of array to 0
		copy[x] *= product #copy contains the left product already
		product *= nums[x]

	return copy
```

**Basic Example**:
```
nums = [1, 2, 3, 4]
```

The solution above finds all the left products of a number and the all the right products.
+ Left product is the product of all the numbers left to it (not including).
+ The left product of 1 is 1, while the left product of 4 is `1*2*3 = 6` .

This is what the first loop does, keeps track of the previous number's left product and factors in *that* number afterwards. 

The right product is the same way except it is not calculated separately. 