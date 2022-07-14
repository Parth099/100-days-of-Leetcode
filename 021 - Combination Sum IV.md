| **Date** | **Link**                                                  | Difficulty |
| -------- | --------------------------------------------------------- | ---------- |
| 7-14-22  | [P377](https://leetcode.com/problems/combination-sum-iv/) | *Medium*   |

# Combination Sum IV
## Bruteforce

Type: Worst case runtime is $O(n^n)$

```python
def combinationSum4(nums: int, target: list[int]):

	#recursive
    def helper(currentChain: tuple[int]):
        currentChainSum = sum(currentChain)

        if currentChainSum == target:
            return 1

        if currentChainSum > target:
            return 0

        count = 0
        for num in nums:
            #attemp a new chain per number in list
            count += helper((*currentChain, num))
            #`*` operator is like the spread operator in js `...`

        return count

    #starter arg : empty tuple 
    return helper(tuple())
    #we could just write helper(()) but thats less readble
```

> "Average DFS Approach"

This code needs no explanation. It will try **each** possible chain until it fails. By failure, I mean going over the target value. 

## DP : Tabular

Type: $O(n^2)$ runtime, $O(n)$ space. 

```python
def combinationSum4(nums: int, target: list[int]):
    dp = [0] * (1 + target)

    for i in range(1, 1 + target):
        numWays = 0
        for num in nums:
            #if the number we are on is a number that is usable directly
            if num == i:
                numWays += 1
            
            if num < i:
                numWays += dp[i - num]

        dp[i] = numWays


    return dp[-1]
```

This solution uses the number of ways the make the numbers before to find all the ways to create the `target` number. I could replace the `numWays` with `dp[i]` but this is a lot more readable. 


First DP problem I solved on my own :) 

### Improvement on DP
```python
def combinationSum4(nums: int, target: list[int]):
    dp = [0] * (1 + target)
    nums.sort() #early break
    for i in range(1, 1 + target):
        for num in nums:
            #if a raw num exists
            if num == i:
                dp[i] += 1
            elif num < i:
                dp[i] += dp[i - num]
            else:
	            #anything after this number will be larger and we wont be able to util prev results
                break 

    return dp[-1] #or dp[target]
```

Sorting allows us to check less items. 