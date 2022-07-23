| **Date** | **Link**                                        | Difficulty |
| -------- | ----------------------------------------------- | ---------- |
| 7-23-22  | [P55](https://leetcode.com/problems/jump-game/) | *Medium*   |

# Jump game
## Bruteforce

Type: $O(n^n)$ with $O(1)$ space requirement

```python
def canJump(nums):

    def helper(currentIndex):

        #if we hit the last index just stop
        if currentIndex == STOPING_POINT:
            return True

        #we must try to take take some steps. if we are on a zero this part is skipped
        #we need the +1 since if we allow 0s it will just loop inf. 
        for step in range(1, nums[currentIndex] + 1): #the number we are on is the max steps we can take

            # first we check if we can even take the step
            # then we see the result of that step
            # while this is a bit shorthand (hides a few details) it is more eff than storing results
            # saves us a variable and a bool check
            if currentIndex + step <= STOPING_POINT and helper(currentIndex + step):
                return True
                

        return False #by default its false 


    STOPING_POINT = len(nums) - 1
    return helper(0)
```

Read comments for more information. 
Understanding of the problem is required. 

## Bruteforce - Memo
Type: $O(n^2)$ runtime with $O(n)$ space. 

```python
def canJump(nums):
    N = len(nums)

	#for coverage
    if N == 1 and nums[0] != 0:
        return True

    dp = [False] * N

    #need the +1 due to zero based indexing
    for initialStep in range(min(N, 1 + nums[0])):
        dp[initialStep] = True #mark all the stops we can access with the init jumps

    for i in range(1, N - 1): #each index except last
        if not dp[i]:
            continue #if we cant access this stop ignore where it will take us

        #need the +1 due to zero based indexing
        #to see why wonder what happens when nums[i] = 1
        for j in range(1 + i, min(N, 1 + i + nums[i])):
            dp[j] = True #mark all the spots we can access with now jump

    return dp[-1]
```

With this approach I really did think that it would pass under the time limit but this did TLE. 

The way this one works is that first you markdown each index you can access from the starting index. And then jump on those times to see where you can end up. If a tile is marked to be non accessible you do not use it; this is because if it was accessible it would have been marked so by previous jumps.  

## DP

Type: $O(n)$ runtime with $O(1)$ space

```python
def canJump(self, nums):
	LIMIT = len(nums) - 1 #to skip the last index
	maxReach = 0 #we cant reach anything from here
	for i in range(LIMIT):
	    if i > maxReach:
	        return False #we got to a point that is unreachable by prev points
	    
	    maxReach = max(maxReach, i + nums[i])

		#this conditional is OPTIONAL
	    if maxReach >= LIMIT: #more eff this way
	        return True #if at any point we can reach the end
	    
	return maxReach >= LIMIT
```

In this approach we keep track of the highest point at a given point and we only stop if we access a tile we should not be able to. 

**Formally**:

Suppose you are on tile $k$ and the max reach from all the tiles before $k$ is $M$. Now if $k \gt M$, we know that it is not possible to get to the end as we cant even get to $k$. If however $k \geq M$ and $\text{nums}[k] \neq 0$ we can keep going. The zero part is ignored in the code because it is resolved by the $\max$ function. Also, if $k = M$, and $\text{nums}[k] = 0$, the loop will terminate and return $\text{false}$ anyway next iteration.  