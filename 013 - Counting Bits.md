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

## Alternate *Similar* Solution 
```py
def countBits(self, num):
	result = [0] * (num + 1) #array of all 0s
    
	for n in range(1, num + 1):
    	result[n] = result[n >> 1] + (n & 1)
            
	return result
```

Recall that each integer is in one the forms:
+ 2**n**+1
+ 2**n**

If we know how many `1`s **n** has we know how many zeros 2**n** has, the same amount. That is what the `n >> 1` represents. 

> 0 is excluded because we need one known value and it does not matter but it was a wasted iteration. 