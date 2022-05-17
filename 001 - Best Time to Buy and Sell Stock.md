| **Date**    | **Link**                                                               | Difficulty |
| ----------- | ---------------------------------------------------------------------- | --------- |
| May 15 2022 | [#121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | *Easy*    | 

# Best Time to Buy and Sell Stock
## Bruteforce 

Type: **O**(n\*n)

````py
def maxProfit(self, prices):
	"""
	:type prices: List[int]
	:rtype: int
	"""
	sellMax = 0
	for today in range(len(prices)):
		for day in range(today +1, len(prices)):
			#profit if we sold today
			sellMax = max(sellMax, prices[day] - prices[today])
	return sellMax
````

Bruteforce times out.

## Optimal Solution

Type: **O**(n)

```py
def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    maxProfit = 0
    lowestNumberSoFar = prices[0]

    for price in prices:
        lowestNumberSoFar = min(lowestNumberSoFar, price)
        maxProfit = max(maxProfit, price - lowestNumberSoFar)
        
    return maxProfit
```

**Explanation**

At each step of the iteration we have the current smallest number seen so far. Thus we can check the profit if we sold it each day given by the quantity `price - lowestNumberSoFar`. 