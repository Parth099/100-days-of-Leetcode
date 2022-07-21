| **Date** | **Link**                                               | Difficulty |
| -------- | ------------------------------------------------------ | ---------- |
| 7-20-22  | [P213](https://leetcode.com/problems/house-robber-ii/) | *Medium*   |

# House Robber II
## DP Solution
```python
def rob(houses):

    def simpleRob(start, end, nums):
        
        #we can do this since the length is atleast 3

		#this is the edge case where we can rob the 1st house from the 3rd
		#hard coded since we dont want to write a if statement in the loop
        nums[start + 2] += nums[start]

        for i in range(start + 3, end):
            nums[i] += max(nums[i - 2], nums[i - 3])

        return max(nums[end-1], nums[end-2])


    N = len(houses)

    if N < 4:
        return max(houses)

    robfirst = simpleRob(0, N - 1, houses[:]) #make copy as the first call will overwrite arrays
    robsecond = simpleRob(1, N, houses[:])

    print(robfirst, robsecond)
    return max(robfirst, robsecond)
```

Same as [[022 - House Robber]]

We can use the same algorithm but stop and start at diff points.

Note: In 022 I use a backwards approach but here I tried a forwards loop. Both approaches work the same. 