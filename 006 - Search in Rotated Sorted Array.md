| **Date**    | **Link**                                                             | Difficulty |
| ----------- | -------------------------------------------------------------------- | ---------- |
| May 25 2022 | [#33](https://leetcode.com/problems/search-in-rotated-sorted-array/) | *Medium*   | 

Related to Problem **005**

# Search in Rotated Sorted Array
## Optimal Solution

Type: **O**(`log n`)

```py
def search(self, nums, target):

	low, high = 0, len(nums) - 1

	while low <= high:
		mid = (low + high) // 2 #or bitwise right shift >> 1
 		if target == nums[mid]:
			return mid
		
		#middle index ruled out
		
		if nums[low] <= nums[mid]:
			#index low to mid is sorted
			if nums[low] <= target < nums[mid]:
				high = mid - 1
			else:
				low = mid + 1
		else:
			if nums[mid] < target <= nums[high]:
				low = mid + 1
			else:
				high = mid - 1

	return -1
```

### Branching
The statement below if true tells is that `arr[low:mid]` is sorted:
```py
nums[low] <= nums[mid]
```

Now if `target` is in between these two element we can shrink our bounds: `low, high`. As the target must be contained in subarray `nums[left:mid]`. Now if it happens that the array is sorted in this interval **and** the target is not in the sorted zone it must be in the other zone (to the right of `mid`).

This same thought process is employed for the other side of the array if sorted. 

### Will the loop terminate?
The simple answer is yes, this is because the bound will change every iteration. Notice that high is only ever decreasing and low is always increasing. Thus, it will **always** terminate.


Another Solution that encompasses the same idea: [Recursive Answer](https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/587261/Python-recursion-O(log-n)-11-lines-easy-to-understand)

## Mirror Solution
Checks right first

```py
def search(self, nums, target):

	left, right = 0, len(nums) - 1

	while left <= right:

		mid = (left + right) // 2 
		if nums[mid] == target:
			return mid

		if nums[mid] <= nums[right]:
			if nums[mid] <= target <= nums[right]:
				left = mid+1
			#not in the right sorted zone
			else:
				right = mid - 1
		else:
			if nums[left] <= target <= nums[mid]:
				#in left sorted zone
				right = mid - 1
			else:
				#not in left sorted zone
				left = mid + 1

	return -1 # does not exist
```