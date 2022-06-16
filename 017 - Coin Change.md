| **Date**     | **Link**                                           | Difficulty |
| ------------ | -------------------------------------------------- | ---------- |
| June 16 2022 | [P332](https://leetcode.com/problems/coin-change/) | *Medium*     |
 
 # Coin Change
 ## Brute Force
 
 Type: $O(n^n)$
 

 ```python
def coinChange(self, coins: list[int], amount: int) -> int:
     
	#satisfy test
	if amount == 0:
		return 0

	#count = 1 as we use the first set of coins here
	cc = [self.helper(coins, amount - coin, 1) for coin in coins]
	result = min(cc)
	return result if result != float('+inf') else -1


def helper(self, coins: list[int], rem: int, count: int):
	#we hit the target
	if rem == 0:
		return count

	# largest value for values that are not possible
	if rem < 0:
		return float('inf')

	count += 1
	cc = [self.helper(coins, rem - coin, count) for coin in coins]
	return min(cc)
 ```
 
 This is a Bruteforce backtracking algorithm that tries each possible combination of coins. 
 
 ## Dynamic Programming - *Bottom Up*
 
Type: $O(n \cdot m) \implies O(n^2)$

```python
def coinChange(self, coins: list[int], amount: int) -> int:
    #create table
    dp = [0] + [float('inf')] * amount
    
    #calulate values for each number from 1 to amount
    for c in range(1, amount + 1): #+1 needed for 0-indexing
        for coin in coins:

            #ignore if coin is larger than the amount of money we needed
            if c - coin >= 0:
				#first iteration, dp[c] = +inf
            	dp[c] = min(dp[c], 1+dp[c-coin]) #+1 since we used a coin there

    return dp[amount] if dp[amount] != float('inf') else -1
```

The array `dp` at index $i$ keeps track of the min coins to make $i$ cents. The code is really self explanatory. At each index it checks if the amount of coins uses to make `index` cents can be reduced by using a *larger* coin. 

## Dynamic Programming - *Top Down*

Type: $O(n \cdot m) \implies O(n^2)$

```python
def coinChange(self, coins: list[int], amount: int) -> int:
    #nested function to avoid having to pass round coins:[int]
    def cacheChecker(amt, cache):
        if amt == 0:
            return 0
        
        elif amt < 0:
            return float('inf')

        elif amt in cache:
            return cache[amt]

        cache[amt] = min(1 + cacheChecker(amt - coin, cache) for coin in coins)
        return cache[amt]

    count = cacheChecker(amount, {})
    return -1 if count == float('inf') else count 
```

Much like *Bottom up*, we use each coin to see if we can reduce the number of overall coins used.  Because we attempt use all combos of coins we can ensure that each entry of cache holds the least amount of coins used. Notice that the cache is set with the min value after using each coin in the amount first. 

Consider `amt = 5, coins = [1, 2]`

Lets look at the call tree for this:
```c
                5
              /   \
             4     3 -> cache hit (one of many)
	    / \   / \
	   3   2 .   .
          / \
         1   2
         |   |
return:  0   0	  
```

This is the order of calls seen by `cacheChecker()`. Now when it calls for `3` for the first time. It will break it down into `1` and `2`. Since those are the coins we can use they will cached as `1`, since we only need one coin. Thus `3` will be put in the cache as using two coins. Now that we know `3` if `3` is called again it will be recalled faster. 
