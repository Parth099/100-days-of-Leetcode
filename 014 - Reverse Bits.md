| **Date**     | **Link**                                                        | Difficulty |
| ------------ | --------------------------------------------------------------- | ---------- |
| June 12 2022 | [P190](https://leetcode.com/problems/reverse-bits/submissions/) | *Easy*     |

# Reverse Bits
## Optimal Solution

Type: **O**(1)

> The loop runs **32** times regardless the number

```py
def reverseBits(self, n):
	out = 0
    for i in range(32):
    	out = (out << 1) | (n & 1)
	    n >>= 1
    return out
```

The code is really self explanatory.

First we get the first bit of `n` and concatenate it on `out`. The concatenation happens by shifting out by one bit to the left and *or*-ing it with the last bit of `n`. If the bit is active it will be shown in `out`. Each iteration `n` is shifted right one so a new bit can be checked. 


> Notice that `n & 1` can only be one or zero.

The `|` operator can be replaced with xor or plus and the output will be the same. 
