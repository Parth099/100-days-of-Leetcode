| **Date** | **Link**                                                           | Difficulty |
| -------- | ------------------------------------------------------------------ | ---------- |
| 7-05-22  | [P1143](https://leetcode.com/problems/longest-common-subsequence/) | *Medium*   |

# Longest Common Subsequence
## Bruteforce 

Type: $O(2^n)$ where $n$ is the length of the smaller string

```python
def longestCommonSubsequence(s1, s2):
    
    # returns the max LCS by considering each possiblity 
    #
    # if the letters match it will take a step forward in both strings 
    # if not, it will take a step forward in both strings separately and compute each possiblity AGAIN

    def helper(s1_i, s2_i, LenLCS):
        if s1_i == L1 or s2_i == L2:
            return LenLCS #string finished

        shifts1, shifts2 = 0, 0

        if s1[s1_i] == s2[s2_i]:
            shifts1 = helper(s1_i + 1, s2_i + 1, LenLCS + 1) #step FWD for both
        else:
            shifts1 = helper(s1_i + 1, s2_i, LenLCS) #seek s1
            shifts2 = helper(s1_i, s2_i + 1, LenLCS) #seek s2

        return max(shifts1, shifts2)

    L1, L2 = len(s1), len(s2)

    return helper(0, 0, 0)
```

## Memo

```python
def longestCommonSubsequence(s1, s2):
    
    # returns the max LCS by considering each possiblity 
    #
    # if the letters match it will take a step forward in both strings 
    # if not, it will take a step forward in both strings separately and compute each possiblity AGAIN

    def helper(s1_i, s2_i):
        if s1_i == L1 or s2_i == L2:
            return 0 #string finished

        if memo[s1_i][s2_i] >= 0:
            return memo[s1_i][s2_i]

        shifts1, shifts2 = 0, 0

        if s1[s1_i] == s2[s2_i]:
            shifts1 = 1 + helper(s1_i + 1, s2_i + 1) #step FWD for both
        else:
            shifts1 = helper(s1_i + 1, s2_i) #seek s1
            shifts2 = helper(s1_i, s2_i + 1) #seek s2

        memo[s1_i][s2_i] = max(shifts1, shifts2)
        return memo[s1_i][s2_i]

    L1, L2 = len(s1), len(s2)
    memo = [[-1 for _ in range(L2)] for _ in range(L1)]
    return helper(0, 0)
```

It saves function calls in an array to allow recall for later. `memo[p][q]` saves the largest common subsequence up to index `p` of `s1` and `q` of `s2`.


## DP - Bottom UP

Type: $O(n * m)$ for both runtime and space

```python
def longestCommonSubsequence(s1, s2):
    L1, L2 = len(s1), len(s2)
    memo = [[0 for _ in range(L2 + 1)] for _ in range(L1 + 1)] 
	#memo with extra padding to avoid if statements
    
    for i in range(L1 - 1, -1, -1):
        for j in range(L2 - 1, -1, -1):
            if s1[i] == s2[j]:
                memo[i][j] = memo[i+1][j+1] + 1
            memo[i][j] = max(memo[i][j], memo[i+1][j], memo[i][j+1])

    return memo[0][0]
```

## DP Top-down
This will be explained as it is much more intuitive.

```python
def longestCommonSubsequence(s1, s2):
    L1, L2 = len(s1), len(s2)
    memo = [[0 for _ in range(L2 + 1)] for _ in range(L1 + 1)] #memo with extra padding to avoid if statements
    
    for i in range(L1):
        for j in range(L2):
            if s1[i] == s2[j]:
                memo[i+1][j+1] = memo[i][j] + 1
            else:
                memo[i+1][j+1] = max(memo[i][j + 1], memo[i + 1][j])

    return memo[-1][-1]
```

The basis for understand is that `memo[i][j]` keeps track of the longest string having considered `i` and `j` chars of `s1` and `s2` respectively. This is why there is extra padding on the memo to ask the question about the longest string having seen the entirety of both strings.

Consider the point `memo[i+1][j+1]`. It can one of three things:

+ The previous indexes `(i, j)` matched and this we continued the chain from there. 

When `(i, j)` do not match it is more interesting. When `i, j` do not match we must increment them separately. 

```py
max(memo[i][j + 1], memo[i + 1][j])
```

What this says is that get me the biggest subsequence length by altering where we are in the string. That is we ask for the biggest string by moving one index forward in s1 and s2 **separately**. This is what we are doing here. 

Suppose we have:

| Var | Value   |
| --- | ------- |
| s1  | 'abcde' |
| s2  | 'ace'   |

Suppose we ask for `memo[3][2]`. That is what is the largest subsequence up to the `d` and `e` non inclusive. 
Well to answer this question we would need `memo[2][2]` and `memo[3][1]` which is the largest subsequence up to `c, e` and `d, c` respectively. 

Note that we need this because they (`d, e`) **do not match**.  

If indexes get confusing here is the same code with index shifted to put the padding on the other side of the memo
```py
def longestCommonSubsequence(s1, s2):
    L1, L2 = len(s1), len(s2)
	#memo with extra padding to avoid if statements
    memo = [[0 for _ in range(L2 + 1)] for _ in range(L1 + 1)] 
    
    for i in range(1, L1+1):
        for j in range(1, L2+1):
            if s1[i - 1] == s2[j - 1]: #current letters match
                memo[i][j] = memo[i-1][j-1] + 1 #set next chain to be one more 
            else:
				#consider left and above
                memo[i][j] = max(memo[i-1][j], memo[i][j-1])

    return memo[-1][-1]
```

