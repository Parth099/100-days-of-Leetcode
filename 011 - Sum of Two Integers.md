| **Date**    | **Link**                                                   | Difficulty |
| ----------- | ---------------------------------------------------------- | ---------- |
| June 8 2022 | [#371](https://leetcode.com/problems/sum-of-two-integers/) | *Medium*   |

# Sum of Two Integers
## Optimal Solution

Type: O(`1`)

```java
public int getSum(int a, int b) {
	//an int is 4 bytes: 32 bits
	while(b != 0){ //carry
        int temp = a ^ b;
		b = (a & b) << 1;   
		
        a = temp;
	}
	return a;
}
```

> Code is in Java because it is easier to do bitwise ops.

**Process**:

The process is essentially recursive but it is faster iteratively. 

```java
//this works just fine too
public int getSum(int a, int b) {
    //an int is 4 bytes: 32 bits
	return (b == 0) ? a: getSum(a ^ b, (a & b) << 1);
}
```

Addition of two numbers has two parts:
- The regular addition part
- The carry

Here is an example to motivate this 

```c
7 = 111
5 = 101
  
    111
+   101
_______
    010 //(A)
   1010 //(B)  
```

Notice that `(A)` is just the addition with no carry, we ignore the carry bits. `(B)`  completes the carry part. 

`(A)` requires us to get the sum without carry and this we can use `xor`. A digit is 1 if the two entries in `a` and `b` are different and `0` if they are the same. That is what an `xor` will do for us. The carry part is not that much harder. We only have a carry digit if both entries are the same number, `1`. Thus we `&` the two values. A `<< 1` is required as you add carry values one digit after the current place. This process needs to be repeated until the carry value is empty (`0`) and the sum will remain unchanged. 