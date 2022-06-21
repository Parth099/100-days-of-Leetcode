| **Date**     | **Link**                                           | Difficulty |
| ------------ | -------------------------------------------------- | ---------- |
| June 13 2022 | [P300](https://leetcode.com/problems/longest-increasing-subsequence/) | *Medium*     |

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

## Dynamic Programming Solution
To be finished when I learn more DP