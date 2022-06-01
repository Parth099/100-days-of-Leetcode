| **Date**    | **Link**                                   | Difficulty |
| ----------- | ------------------------------------------ | ---------- |
| June 1 2022 | [#11](https://leetcode.com/problems/container-with-most-water/) | *Medium*   |

# Container With Most Water
## Optimal Solution
```py
def maxArea(self, heights):
	"""
	:type height: List[int]
	:rtype: int
	"""
	head, tail = 0, len(heights) - 1
	globalMax = float('-inf')
	currContainerHeight = 0
	while head < tail:
		currContainerHeight = min(heights[head], heights[tail])
		#print(heights[head], heights[tail])
		#height * width
		globalMax = max((tail - head) * currContainerHeight, globalMax)

		if heights[head] < heights[tail]:
			currHead = heights[head]
			while currHead >= heights[head] and head < len(heights) - 1:
				head += 1 #moves up until we find a new max

		elif heights[head] > heights[tail]:
			currTail = heights[tail]
			while currTail >= heights[tail] and tail > -1:
				tail -= 1 #moves up until we find a new max

		else: #both equal
			head, tail = head + 1, tail - 1
            
return globalMax
```

We start at the maximum distance between container walls (`head, tail`). This is because we can then decrease in height for a gain in width. The area component is evidently saved in `globalMax`. 

Now if the head height is shorter than tail. We need to move rightwards. Since right bound is greater we can gain more height if we move left (maybe). The leftward movement is the same idea.

The looping for moving `head` and `tail` is more complex than it needs to be because this allows us to skip values. 

Consider this array:
```py
heights = [1,8,6,2,5,4,8,3,7]
```

We see at first that **1** and **7** are the bounds. Since `1 < 7` we must move right from head. We get to **8** since that is the next largest number after **1**. Then we move the right bound from **7** to **8**. After it ends since the loop skips over smaller *unnecessary* values.