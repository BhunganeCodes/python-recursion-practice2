from solutions.recursion_advanced import (
    countdown,
    power,
    count_occurrences,
    is_palindrome,
    gcd,
    binary_search,
    sum_digits,
    max_in_list,
    permutations_count,
    tower_of_hanoi_moves
)

# 1. Countdown
def test_countdown():
    assert countdown(3) == [3, 2, 1]
    assert countdown(1) == [1]
    assert countdown(0) == []
    assert countdown(5) == [5, 4, 3, 2, 1]
    assert countdown(-1) == []

# 2. Power
def test_power():
    assert power(2, 0) == 1
    assert power(2, 3) == 8
    assert power(5, 1) == 5
    assert power(3, 4) == 81
    assert power(10, 2) == 100

# 3. Count occurrences
def test_count_occurrences():
    assert count_occurrences([], 1) == 0
    assert count_occurrences([1, 2, 3], 2) == 1
    assert count_occurrences([1, 1, 1], 1) == 3
    assert count_occurrences([4, 5, 6], 7) == 0
    assert count_occurrences([2, 2, 2, 2], 2) == 4

# 4. Palindrome check
def test_is_palindrome():
    assert is_palindrome("") is True
    assert is_palindrome("a") is True
    assert is_palindrome("racecar") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("madam") is True

# 5. Greatest Common Divisor
def test_gcd():
    assert gcd(10, 5) == 5
    assert gcd(14, 7) == 7
    assert gcd(48, 18) == 6
    assert gcd(7, 3) == 1
    assert gcd(20, 8) == 4

# 6. Binary search
def test_binary_search():
    nums = [1, 3, 5, 7, 9]
    assert binary_search(nums, 1) == 0
    assert binary_search(nums, 9) == 4
    assert binary_search(nums, 5) == 2
    assert binary_search(nums, 2) == -1
    assert binary_search(nums, 10) == -1

# 7. Sum of digits
def test_sum_digits():
    assert sum_digits(0) == 0
    assert sum_digits(7) == 7
    assert sum_digits(123) == 6
    assert sum_digits(999) == 27
    assert sum_digits(1001) == 2

# 8. Maximum in list
def test_max_in_list():
    assert max_in_list([1]) == 1
    assert max_in_list([1, 5, 3]) == 5
    assert max_in_list([-1, -5, -3]) == -1
    assert max_in_list([10, 20, 30, 5]) == 30
    assert max_in_list([7, 7, 7]) == 7

# 9. Permutations count
def test_permutations_count():
    assert permutations_count(0) == 1
    assert permutations_count(1) == 1
    assert permutations_count(2) == 2
    assert permutations_count(3) == 6
    assert permutations_count(5) == 120

# 10. Tower of Hanoi moves
def test_tower_of_hanoi_moves():
    assert tower_of_hanoi_moves(0) == 0
    assert tower_of_hanoi_moves(1) == 1
    assert tower_of_hanoi_moves(2) == 3
    assert tower_of_hanoi_moves(3) == 7
    assert tower_of_hanoi_moves(4) == 15
