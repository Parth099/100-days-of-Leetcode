| **Date**  | **Link**                                          | Difficulty |
| --------- | ------------------------------------------------- | ---------- |
| 7-21-22 | [P91](https://leetcode.com/problems/decode-ways/) | *Medium*   |


# Decode Ways
## Bruteforce

Type: $O(2^n)$ runtime with $O(1)$ space

```python
def numDecodings(s: str):
    def helper(index):
        if index == N:
            return 1

        #handle next letter
        one, two = 0, 0
        if s[index] != '0':
            one += helper(index + 1)
            
		#handle next two letters
        if index + 2 <= N and s[index: index + 2] in letterCache:
            two += helper(index + 2)

        return one + two 

    letterCache = {str(i) : 0 for i in range(1, 27)}
    N = len(s)
    return helper(0)
```

This block looks at each possible variation of the string and counts up the possible ways we can decode it. Now at each stage we ask what is the num. ways we can decode the string from *here*. This subproblem is then used to solve the overall problem of the entire string.

Example:

Consider `s = '127'`

```c
                 s
                / \  
               1  12
              / \   \
             27  2   7
                  \ 
                   7
```

Ignore the order of the nodes. But this is how the code above operates. It will determine that:
```java
(1, 27)   -> invalid
(1, 2, 7) ->   valid
(12, 7)   ->   valid
```

## DP - *Bottom Up*

Type: $O(n)$ runtime with $O(n)$ space

```python
#on leetcode put this OUTSIDE the class 
letterCache = {str(i) : 0 for i in range(1, 27)}
def numDecodings(s: str):
    
    N = len(s)
    dp = {N : 1} #for the inital iteration (we can decode one letter only one way)

    for i in range(N - 1, -1, -1):
        if s[i] == '0':
            dp[i] = 0
        else:
            dp[i] = dp[i + 1]

        #at this point dp[i] ALREADY has a value so we can use +=
        if i + 1 < N and s[i:i+2] in letterCache:
            dp[i] += dp[i + 2]

    return dp[0]
```

Consider the string `216`. 

If we wanted to find all ways this could be decoded we would need to know how many ways `16` and `6` could be decoded. 

We know that `16` can be decoded as `(1, 6)` and `(16)`. 

Now we just have to introduce the `2`. The two can go with the ways `16` can be decoded, which is 2. 
We also note that `21` can also be a starter string. Thus, it goes with `6`. 

This is all of the three ways. 


**How the DP does it**:

We start at the end of the string. Notice that we can only make one string here. 
Next we move one index back. Here we can either make a string of length 2 or 1. We look back and combine the results from the prev calcs. 

This is why we keep an array of subproblems so we can look backward to combine results. 