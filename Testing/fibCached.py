cache = {0 : 0, 1 : 1,}
import time

start = time.perf_counter()

def fib(n):
    def _fib(k):
        return fib(k - 1) + fib(k - 2) # classic
    if n not in cache:
        cache[n] = _fib(n) #bruteforce assisted calc
    return cache[n]

end = time.perf_counter()
print(fib(100))
print(end-start)