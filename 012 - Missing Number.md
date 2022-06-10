| **Date**    | **Link**                                                   | Difficulty |
| ----------- | ---------------------------------------------------------- | ---------- |
| June 9 2022 | [#268](https://leetcode.com/problems/missing-number/) | *Easy*   |

# Missing Number
## Solution One

Type: **O**(n)

```py
def missingNumber(self, nums):
	length = len(nums)
	sumOfFirstNInts = (length * (length + 1)) / 2
	diff = sumOfFirstNInts - sum(nums)
        
	return diff 
```

The problem gives us a non sorted array and asks us to find the missing number from a range from `[0, n]` where any number can be missing inclusive. This approach is the simplest. It adds up all the number and subtracts that from the sum of the first `n` integers. The difference is the missing number, which can be 0. 

## Solution 2

Type: **O**(n)

```py
def missingNumber(self, nums):
        
	missing = len(nums)
        
	for index in range(0, len(nums)):
        missing ^= index
		missing ^= nums[index]
            
	return missing
```

Recall these properties of *xor*.
```py
a^b^b = a

a^a = 0
```

This is true regardless of the order of the numbers.

What the loop does is xor each number and each value of the array (of course):
```c
0 ^ 1 ^ ... ^ n ^ a1 ^ ... ^ an
```

 Notice that each number *should* have 2 copies. One from the array and one from the loop counter. This is true for all numbers except the end number. 
 
 > See that in the array `[0, 1, 2]` , `3` is missing. This is why it is set as the missing var initially. 

Anyways, we xor each index and array entry and any number that has no pair should be singled out as `a ^ a = 0` and each number has a pair except the missing one. 