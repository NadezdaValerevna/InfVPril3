# my_lib.py
import numpy as np

# Функция определения чисел Фибоначчи
# Принимает n чисел
# Возвращает список последовательности Фибоначчи = n
# Пример: n = 7 => [0 1 1 2 3 5 8]
def fibonacci(n):
    if n <= 0:
        raise ValueError("need n > 0")
    fib_arr = np.zeros(n)
    fib_arr[1] = 1
    for i in range(2, n):
        fib_arr[i] = fib_arr[i - 2] + fib_arr[i - 1]
    return fib_arr

# Функция сортировки массива Пузырьком
# Принимает массив чисел
# Возвращает отсортированный массив
# Пример: [4 2 3 1] => [1 2 3 4]
def bubble_sort(array):
    if len(array) <= 0:
        raise ValueError("Null array")
    if len(array) <= 0:
        raise
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] < array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    return array

# Решето Эратосфена
# Принимает число до которого будет находить простые числа
# Возвращает список простых чисел
# Пример: 3 => [2 3 5]
def eratosthenes(n):
    if n <= 0:
        raise ValueError("need n > 0")
    primes = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    prime_numbers = [p for p in range(2, n + 1) if primes[p]]
    return prime_numbers


