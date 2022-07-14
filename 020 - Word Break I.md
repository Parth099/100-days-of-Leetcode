| **Date** | **Link**                                                           | Difficulty |
| -------- | ------------------------------------------------------------------ | ---------- |
| 7-10-22  | [P129](https://leetcode.com/problems/word-break/) | *Medium*   |

# Word Break I
## Bruteforce 

```python
def wordBreak(s: str, wordDict: list[str]) -> bool:
    
    def helper(newS):

        #assume word break is not possible
        result = False

        if not newS:
            return True

        for word in wordDict:
            N = len(word)

            #if too big; ignore
            if N > len(newS):
                continue

            #if possible; try it!
            if word == newS[:N]:
                #or the result with each result below it; if it is truly not possible it will be false
                result |= helper(newS[N:])
                if result:
                    return True #no need for further calcs 

        return result
    
    return helper(s)
```

This method much like the other bruteforce methods uses DFS. It tries each *possible* combination of words from `wordDict`.  

Note about Python string slicing
```text
s = '012345'
s[:1] => "0"    , the second number represents upto
s[1:] => "12345", the first  number represents from
```


## Bruteforce - Index Based
```python
def wordBreak(s: str, wordDict: list[str]) -> bool:

    def helper(index: int):

        #assume we cant break it down
        result = False

        #if we are able to map over the entire string
        if index >= N:
            return True

        for word in wordDict:
            M = len(word)

            if index + M > N: #if the string is too big to fit 
                continue #ignore it
                
			#potential speed up here if we write our own strcmp for our custom logic
            if s[index: index + M] == word: 
                result |= helper(index + M)

        return result

    
    N = len(s)
    return helper(0)
```

Same concept as before, if a word from the dict fits, we launch off a new thread.

> Not really a thread but we can think of it that way.

## DP - Bottom Up 

Type: $O(n * m)$ runtime with $O(n)$ space

```python
def wordBreak(s: str, wordDict: list[str]) -> bool:

    N = len(s)

    #N+1 since we need an entry for the base case of the empty string ""
    dp = [False] * (N+1) 
    dp[N] = True 

    for i in range(N, -1, -1):
        for word in wordDict:
            M = len(word)
            if i + M > N:
                continue #too big to match
                
            if s[i:i+M] == word:
                dp[i] = dp[i + M]
                
            if dp[i]:
                break
    
    return dp[0]
```

Starting from the back it considers if a word can fill the gap from the current index to the end of the string. From the back it builds up a *database* of indexes where if they are able to get to a certain index then it is possible to build the bat. 

It is easier to explain with example. 

Consider params:
```python
s = "subzero"
wordDict = ['sub', 'zero']
```

We know that if we get to the end of the word then we have solved the problem. Now starting from the back, we move to `o`. We see that `o` is too small as no words in the dict are of size **1**. So we move until we get to the letter `e`. We compare `e`\* to each word in the dict and see that it **does not match anything**. We move to `z` and see that it matches `zero`. Since that takes us to the end of the string we set `z` to be a point where if we can get back to `z` again, we have broken the word. Now we keep moving, we check `u` and `b` with no luck. Getting to `s`, we see it matches sub and see that it gets us to index, `3` which is `z`. Thus the word can be broken. 

We keep the points on interest in an array which allows us to know *fast* when we can stop searching. 

\* - from `e` to the end of the word