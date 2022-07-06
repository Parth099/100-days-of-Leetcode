| **Date**     | **Link**                                           | Difficulty |
| ------------ | -------------------------------------------------- | ---------- |
| 7-05-22 | [P300](https://leetcode.com/problems/longest-increasing-subsequence/) | *Medium*     |

# Longest Increasing Subsequence
## Bruteforce
Type: $O(2^n)$

> This solution **will** timeout

```python
def lengthOfLIS(nums: list[int]) -> int:
    n = len(nums)
    #back tracker!!
    #compares each subsequent number and desides to add it to the array
    #maxSubSequenceLength is too hard not to keep track of without functional args
    maxLength = 1
    def helper(subSequencelastNumber, subSequenceLength, index):
        #subSequenceLength will never be 0
        
        nonlocal maxLength #non local to ref outside var
        for i in range(index, n):
            #if we see a larger number add it to the list
            if subSequencelastNumber < nums[i]:
                output = helper(nums[i], subSequenceLength+1, i)
                maxLength = max(output, maxLength)
                #return output
        
        # return is hit when subSequenceLength = n; the loop will not run
        return subSequenceLength

    #fire off subprocesses by starting each subseq at each index
    for i in range(n):
        helper(nums[i], 1, i)

    #return the largest one
    return maxLength
```

This algorithm is checks each possible Subsequence by either adding it to the moving list or not. 

Consider the input: `[0, 2, 1, 3]`

This is the initial call sequence\* :
```c
Start : [0]

Recursive call 1 arrays: {[0, 2], [0, 1], [0, 3]}
Recursive call 2 arrays: {[0, 2, 3]} (return 3)
Recursive calls 3 arrays: {[0, 1, 3]} (return 3)
Recursive calls 4 arrays: {[0, 3]} (return 2)

Next: [2]
...
```

## More Compact Bruteforce

Source: [Leetcode](https://leetcode.com/problems/longest-increasing-subsequence/discuss/429079/Python-5-Approaches%3A-Recursion-Recur-%2B-Memo-DP-DP-%2B-Binary-Search-Print-all-LIS)

```python
def lengthOfLIS(nums: list[int]) -> int:
    n = len(nums)
    def helper(lastNum, currIndex):
        if currIndex == n:
            return 0

        add, notAdd = 0, 0
        if nums[currIndex] > lastNum:
            add = 1 + helper(nums[currIndex], currIndex+1)
        notAdd = helper(lastNum, currIndex+1) #continuation
        return max(add, notAdd)

    return helper(float('-inf'), 0)
```

The longest subsequence in `[0:n]` is the same as the longest subsequence in `1 + [1:n]` 

In other words at each index we consider if wish to add the current number to the subsequence. It does this process for each index. 

This is really what the two variables stand for. 
`add` represents the LIS starting at that index while `notAdd` represents the LIS starting at the next index over. 

Consider the array `[5, 1, 2]`. When it looks at `5`, the algorithm will try continuing the subsequence at **each** subsequent index, that is what the `continuation` comment is for.

## Memoization
```python
def lengthOfLIS(nums: list[int]) -> int:

    def helper(prevIndex, currIndex):
        if currIndex == N:
            return 0

		#A
        if memo[prevIndex+1][currIndex] >= 0:
            return memo[prevIndex + 1][currIndex]

        add, notAdd = 0, 0
        if prevIndex < 0 or nums[currIndex] > nums[prevIndex]:
            add = 1 + helper(currIndex, currIndex+1)
            
        notAdd = helper(prevIndex, currIndex+1)
        memo[prevIndex + 1][currIndex] =  max(add, notAdd)
        return memo[prevIndex + 1][currIndex]

    N = len(nums)
    memo = [[-1 for _ in range(N)] for _ in range(N)]
    return helper(-1, 0)
```

The memo just stores function calls. 
Here is how the memo works. The last row of the memo, (row N-1) stores the LIS starting from the last element of the subsequence (which will be 1 or -1 if that slot is never accessed). This memo is filled from bottom right to the top right which corresponds to the `(-1, 0)` call!

### Memo Optimization

```python
def lengthOfLIS(nums: list[int]) -> int:

    def helper(prevIndex, currIndex):
        if currIndex == N:
            return 0

        if memo[prevIndex+1] >= 0:
            return memo[prevIndex + 1]

        add, notAdd = 0, 0
        if prevIndex < 0 or nums[currIndex] > nums[prevIndex]:
            add = 1 + helper(currIndex, currIndex+1)
            
        notAdd = helper(prevIndex, currIndex+1)
        memo[prevIndex + 1] = max(add, notAdd)
        return memo[prevIndex + 1]

    N = len(nums)
    memo = [[-1 for _ in range(N)] for _ in range(N)]
    return helper(-1, 0)
```

We do not need to worry about what the current index is really due to the `max(add, notAdd)` call.



## Dynamic Programming Solution

$O(n^2)$ runtime with $O(n)$ space requirement.

```python
def _lengthOfLIS(nums):
    N = len(nums)
    dp = [1] * N

    for i in range(N - 2, -1, -1):
        for j in range(N - 1, i, -1): 
            if nums[i] < nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])

    return max(dp)

#forward
def lengthOfLIS(nums):
    N = len(nums)
    dp = [1] * N

    for i in range(1, N):
        for j in range(i): #recall range(i) => (0, ..., i - 1) if i >= 1, 
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])

    return max(dp)

```

Per usual DP saves a sub-result and uses it later to solve a larger problem. 

The explanation will be around the `#foward` algorithm. 

We start of with a chain length of **1**. That is the smallest length chain we can have with a non-empty array. Now at each step we check if we can extend a chain from a previous index. That is really it. The DP solution is simple compared to DFS or Memo. 

There exists an $O(n \log n)$  solution. <!-- HAHA -->
