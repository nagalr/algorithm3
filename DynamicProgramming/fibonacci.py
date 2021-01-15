import time


def fibonacci(n):
    if n < 2:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


# the cache
cache = {}
def fibonacci_dynamic(n):
    # base
    if n < 2:
        return n
    # extract from cache, if its there
    if n in cache:
        return cache[n]
    # calculate value into cache, and return it
    else:
        cache[n] = fibonacci_dynamic(n - 1) + fibonacci_dynamic(n - 2)
        return cache[n]


# Testing

print('\n############## MEASURE TIMES NO CACHE N=4 ################')
t1 = time.time()
print('The number for fibonacci(20) is: ' + str(fibonacci(20)))
t2 = time.time()
print('computing time is: ' + str(t2 - t1))

print('\n############## MEASURE TIMES WITH CACHE N=900 ################\n')
t1 = time.time()

print('The number for fibonacci(900) is: ' + str(fibonacci_dynamic(900)))
t2 = time.time()
print('computing time is: ' + str(t2 - t1))
