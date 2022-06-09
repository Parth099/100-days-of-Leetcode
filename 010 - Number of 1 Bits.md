| **Date**    | **Link**                                                | Difficulty |
| ----------- | ------------------------------------------------------- | ---------- |
| June 6 2022 | [#191](https://leetcode.com/problems/number-of-1-bits/) | *Easy*     |


# Number of 1 Bits
## My Solution

```py
def hammingWeight(n):
	"""
    :type n: int
    :rtype: int
    """
    count = 0
    while n:
    	count += n & 1 #checks if ones place bit is active
        n >>= 1 #shift down
	return count 
```

This is quite trivial.

## Alternate Solution

```py
def hammingWeight(n):
	"""
    :type n: int
    :rtype: int
    """
    count = 0
    while n: # n not 0
    	count += 1
        n &= n - 1 # n = n & (n - 1)
	return count 
```

**Explanation**

Essentially each iteration one of the active `1`s is removed. Consider the number `1001`. At first iteration n = `1000` and one of the `1`s is gone. Now next iteration, `n - 1 = 0111`. If we `&=` this, it will name `n = 0`, ending the loop.

Each iteration either it turns off the one's digit or it takes away one of the `1`s and turns all the zeros after that digit place to `1`s. Since in `n` these digits are `0`s, they will get and-ed to 0. 