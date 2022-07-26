# Union Find Operations
## Union Find

| Constructor | Find   | Union  | Space  |
| ----------- | ------ | ------ | ------ |
| $O(n)$      | $O(n)$ | $O(1)$ | $O(n)$ | 

## Quick Find
| Constructor | Find   | Union  | Space  |
| ----------- | ------ | ------ | ------ |
| $O(n)$      | $O(1)$ | $O(n)$ | $O(n)$ | 

## Quick Union
| Constructor | Find   | Union  | Space  |
| ----------- | ------ | ------ | ------ |
| $O(n)$      | $O(n)$ | $O(n)$ | $O(n)$ | 

The $O(f(n))$ notation does not tell the full story here. Quick Union is faster because it only requires **2** `find` calls to make a union. Quick find on the other hand has a loop. 

## Quick Union By Rank
| Constructor | Find         | Union        | Space  |
| ----------- | ------------ | ------------ | ------ |
| $O(n)$      | $O(\log{n})$ | $O(\log{n})$ | $O(n)$ |



- Find is now logarithmic because it will have to search balanced trees.
- Union is logarithmic because the find operations it uses are logarithmic.



