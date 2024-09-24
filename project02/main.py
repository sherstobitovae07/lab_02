def sieve_of_eratosthenes(n):
    # Инициализируем список, где True означает, что число простое
    primes = [True] * (n + 1)
    p = 2
    while p * p <= n:
        # Если primes[p] не было изменено, то оно простое
        if primes[p]:
            # Обнуляем все кратные p начиная с p^2
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    return [p for p in range(2, n + 1) if primes[p]]

n = int(input("Введите число n: "))
prime_numbers = sieve_of_eratosthenes(n)
print(f"Простые числа до {n}: {prime_numbers}")
