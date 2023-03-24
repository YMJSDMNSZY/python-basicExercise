#局部变量只能在函数内存在

import time

# def fibonacci(n):
#     if n < 2:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# start_time = time.perf_counter()
# print(fibonacci(30))
# end_time = time.perf_counter()
# print(f"The execution time: {end_time - start_time:.8f} seconds")
# The execution time: 0.22815740 seconds



from functools import lru_cache
# import time
#
# @lru_cache(maxsize=None)
# def fibonacci(n):
#     if n < 2:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# start_time = time.perf_counter()
# print(fibonacci(30))
# end_time = time.perf_counter()
# print(f"The execution time: {end_time - start_time:.8f} seconds")
# # The execution time: 0.00002990 seconds