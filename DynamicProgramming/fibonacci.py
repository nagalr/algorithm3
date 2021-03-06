import time

# Global variable to count calculations number
calc1 = 0
def fibonacci(n):
    """
    fibonacci sequence calculation Impl.
    Time O(2^n) run, no cache.
    """
    if n < 2:
        return n
    global calc1
    calc1 += 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# Global variable to count calculations number
calc2 = 0
# the cache
cache = {}
def fibonacci_dynamic(n):
    """
    fibonacci sequence calculation Impl.
    Time O(n) run, using cache.
    """
    # base
    if n < 2:
        return n
    # extract from cache, if its there
    if n in cache:
        return cache[n]
    # calculate value into cache, and return it
    else:
        global calc2
        calc2 += 1
        cache[n] = fibonacci_dynamic(n - 1) + fibonacci_dynamic(n - 2)
        return cache[n]


# Testing

print('\n############## MEASURE TIMES NO CACHE N=4 ################')
t1 = time.time()
print('The number for fibonacci(25) is: ' + str(fibonacci(25)))
t2 = time.time()
print('computing time is: ' + str(t2 - t1))
print('number of calculations: ' + str(calc1))

print('\n############## MEASURE TIMES WITH CACHE N=900 ################\n')
t1 = time.time()

print('The number for fibonacci(900) is: ' + str(fibonacci_dynamic(900)))
t2 = time.time()
print('computing time is: ' + str(t2 - t1))
print('number of calculations: ' + str(calc2))


