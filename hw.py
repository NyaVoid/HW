def decorator_function(func):
    def wrapper(a, b, c):
        n = a + b + c
        primes = [i for i in range(n + 1)]
        primes[1] = 0
        i = 2
        while i <= n:
            if primes[i] != 0:
               j = i + i
               while j <= n:
                  primes[j] = 0
                  j += i
            i += 1
        primes = [i for i in primes if i != 0]
        if n in primes:
            print('Простое')
        else:
            print('Составное')
        print(primes)
        func(a, b, c)
    return wrapper

@decorator_function
def sum_three(a, b, c):
    print(a + b + c)
sum_three(2, 3, 6)
