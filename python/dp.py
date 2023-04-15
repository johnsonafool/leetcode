import time

arr = [-1] * (200 + 1)


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)


def dp_fib(n):
    arr[0] = 0
    arr[1] = 1
    for i in range(2, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]
    return arr


start = time.time()
print(dp_fib(200))
end = time.time()
print("cost time: ", end - start)
