| **Date**  | **Link**                                            | Difficulty |
| --------- | --------------------------------------------------- | ---------- |
| 7-15-22🎂 | [P198](https://leetcode.com/problems/house-robber/) | *Easy*   |


# House Robber
## Bruteforce
Type: $O(n^n)$ with $O(1)$ space

```python
def rob(nums: list[int]) -> int:
    
    def helper(index, currentSteal):
        if index >= N:
            return currentSteal

        currentSteal += nums[index] #rob the current house
        maxSteal = currentSteal
        for i in range(index+2, N): #+2 as we cant rob adj houses
            maxSteal = max(maxSteal, helper(i, currentSteal))

        return maxSteal

	N = len(nums)
    return max(helper(0, 0), helper(1, 0))
```

This is the bruteforce approach where each possible scenario is considered. The `return` looks a bit off because if we only consider starting at the first house then the second house is missed. Now the second house by it self could be the most valuable. 

We only have two starting choices because each house contains a positive amount to steal. 

## DP Approach
Type: $O(n^2)$ runtime $O(1)$ Space

```python
def rob(nums: list[int]) -> int:
    N = len(nums)

    #if there are 2 or less houses
    if N < 3:
        return max(nums)

    for i in range(N - 3, -1, -1):
        best_steal = 0
        for j in range(i + 2, N):
            best_steal = max(best_steal, nums[j])
            
        nums[i] += best_steal
        
    return max(nums[0], nums[1])
```

We start from the back collecting the best amounts to steal and then we use the previous results to get the best loot outcome. 

We start at the third last house and keep track of the highest number of money we can steal. Now from the third last house we can only rob the last house so we do so. Then we move the the forth last house. Now we have the option to rob the last house or the second last house. We will, of course, rob the best house. 

### DP Improvement
```python
def rob(self, nums: list[int]) -> int:
        
    N = len(nums)
    if N < 3:
        return max(nums)

    nums += [0] #padding for smaller arrays 
    for i in range(N - 3, -1, -1):
        nums[i] += max(nums[i+2], nums[i+3])
        
    return max(nums[0], nums[1])
```

See that we don't need worry about every house but only the two house after the one we cant rob (adjacent house). This is because the numbers only get larger as we go on, we do not need to check the smaller numbers anyways. 

Note: We can also do this in reverse. Well forward actually. The max results can be stored in the last two spots of the array (`n[-1], n[-2]`). 