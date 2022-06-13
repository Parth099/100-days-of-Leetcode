| **Date**     | **Link**                                              | Difficulty |
| ------------ | ----------------------------------------------------- | ---------- |
| June 13 2022 | [P70](https://leetcode.com/problems/climbing-stairs/) | *Easy*     |

# Climb Stairs
## Optimal Solution

Type: **O**(n)

```py
def climbStairs(self, n: int) -> int:
	a, b = 1, 1
	for i in range(1, n): #starts at 1 since n != 0
		a, b = a+b, a
	return a
```

This problem is a restatement of the fibonacci formula. Suppose we want to get to stair `k`. If we know all the ways to get from stair `k-2` to `k` and `k-1` to `k` then their sum is the total number of ways to get to `k`.

The reason this works is because a person can only take 1 or 2 steps. This either the last step is two-sized or one-sized. 

While this may be a DP problem, caching was not the best solution since this solution has *constant* space while caching requires **O**(n) space.