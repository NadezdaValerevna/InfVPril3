# test_my_lib.py
import pytest
import my_lib


class TestFibonacci:

    # Позитивный тест с корректными данными. Возвращает последовательность Фибоначчи
    def test_positive_fibonacci(self):
        assert my_lib.fibonacci(5).tolist() == [0, 1, 1, 2, 3]

    # Негативный тест с n <= 0. Если мы подаем на вход n <= 0, то программа с последовательностью Фибоначчи выдает ошибку
    # Вызывается исключение ValueError
    def test_negative_fibonacci(self):
        with pytest.raises(ValueError):
            my_lib.fibonacci(0)

class TestBubbleSort:

    # Позитивный тест с корректными данными. Возвращает отсортированный массив
    def test_positive_bubble_sort(self):
        assert my_lib.bubble_sort([1, 9, 5, 3]) == [1, 3, 5, 9]

    # Негативный тест с пустым массивом. Вызывается исключение ValueErrorм
    def test_negative_bubble_sort(self):
        with pytest.raises(ValueError):
            my_lib.bubble_sort([])

class TestEratosthenes:
    # Позитивный тест с корректными данными. Возвращает последовательность простых чисел до 20
    def test_positive_eratosthenes(self):
        assert my_lib.eratosthenes(20) == [2, 3, 5, 7, 11, 13, 17, 19]

    # Негативный тест с n <= 0. Если мы подаем на вход n <= 0, то программа с Решетом Эратосфена выдает ошибку
    # Вызывается исключение ValueError
    def test_negative_eratosthenes(self):
        with pytest.raises(ValueError):
            my_lib.eratosthenes(-1)
