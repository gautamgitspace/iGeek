#!/usr/bin/env python3

"""
pool flavors

pool.apply(f, args): f is only executed in ONE of the workers of the pool.
So ONE of the processes in the pool will run f(args). It is deprecated since
py 2.3

pool.map(f, iterable): This method chops the iterable into a number of chunks
which it submits to the process pool as separate tasks. So you take advantage
of all the processes in the pool.

Pool.apply_async is also like Python's built-in apply, except that the call
returns immediately instead of waiting for the result. An AsyncResult object
is returned. You call its get() method to retrieve the result of the function
call. The get() method blocks until the function is completed. Thus,
pool.apply(func, args, kwargs) is equivalent to
pool.apply_async(func, args, kwargs).get().

In contrast to Pool.apply, the Pool.apply_async method also has a callback which,
if supplied, is called when the function is complete. This can be used instead of
calling get().

"""

from multiprocessing import Pool

def cube(x):
    return x**3

# MAP: retrieval of in-order results? YES. multi-arg? NO, blocking? YES, concurrent? YES
pool = Pool(processes=4)
results = pool.map(cube, range(1,7))
print (results)

# MAP_ASYNCH: retrieval of in-order results? YES multi-arg? NO, blocking? NO, concurrent? YES
pool = Pool(processes=4)
results = pool.map_async(cube, range(1,7))
print (type(results))
print (results.get())

# APPLY: retrieval of in-order results? YES multi-arg? YES, blocking? YES, concurrent? YES
pool = Pool(processes=4)
results = [pool.apply(cube, args=(x,)) for x in range(1,80)]
print (results)

# APPLY_ASYNCH
# retrieval of in-order results, multi-arg? YES, blocking? NO.
# but get call is blocking, concurrent? YES
pool = Pool(processes=4)
results = [pool.apply_async(cube, args=(x,)) for x in range(1,80)]
print (type(results))
output = [result.get() for result in results]
print (output)
