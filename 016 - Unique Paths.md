| **Date**     | **Link**                                           | Difficulty |
| ------------ | -------------------------------------------------- | ---------- |
| June 13 2022 | [P62](https://leetcode.com/problems/unique-paths/) | *Medium*     |
 
# Unique Paths
## Optimal Solution

Type: **O**(1)

> **O**(1) because it does not matter the length of the path. 

```python
def uniquePaths(self, m: int, n: int) -> int:
	#total moves = (n - 1) + (m - 1)
	return comb(n+m-2, min(n, m)-1) #COMBonatoic
```

Say we start at coordinate (0, 0) and wish to make it to (m, n). See that `m+n` total moves must be made. Out of `m+n` moves, `n` of them must be down. Hence the combonatoic.

I have no idea of how `math.comb(n, k)` is implemented. It is likely:
```python
def nCr(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)
```