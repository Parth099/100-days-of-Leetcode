| **Date**     | **Link**                                             | Difficulty |
| ------------ | ---------------------------------------------------- | ---------- |
| June 10 2022 | [#338](https://leetcode.com/problems/counting-bits/) | *Easy*     |

# Counting Bits
## Naive Solution
```py
def count1s(self, n):
	count = 0
    while n:
		count += 1
		n &= n - 1
	return count
    
def countBits(self, n):
	"""
	:type n: int
    :rtype: List[int]
    """
    return [self.count1s(x) for x in range(0, n+1)]
```

Review Problem **010** to see why this would work. 

## Optimal Solution
```py
def countBits(self, num):
	setBits = [0] * (num+1) #array of all 0s
	for i in range(1 ,num+1):
		setBits[i] = setBits[i & (i-1)] + 1
	return setBits
```

The way this works it checks the number of bits of the number the number has if it had one bit less and adds one to it. 

Consider an integer `n`. If we remove an active bit from `n` it **will** be smaller and thus its entry will be in the array already. 

> This is very hard to think of. 