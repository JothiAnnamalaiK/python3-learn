# A function calling itself to solve a problem.

# fibanocci series: 0 1 1 2 3 5 8 13
fib = []


# fibanocci as normal func:
def fibanocci(n):
    for i in range(0, n):
        if i == 0 or i == 1:
            fib.append(i)
        else:
            fibi = fib[i - 2] + fib[i - 1]
            fib.append(fibi)
    return fib


gen_fibanocci = fibanocci(10)
fibanocci_series = ",".join(str(gen_fibanocci))
fibanocci_series = ",".join(str(x) for x in gen_fibanocci)
print("fibanocci: ", fibanocci_series)


# fibanocci as recursive func:
def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


gen_fibanocci = [fibonacci_recursive(i) for i in range(10)]
fibanocci_series = ",".join(str(x) for x in gen_fibanocci)
print("Fibonacci (recursive):", fibanocci_series)
