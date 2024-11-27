from tasks.task4_max import find_max

def test_find_max():
    assert find_max([3, 1, 4, 1, 5, 9]) == 9
    assert find_max([-3, -1, -4, -1, -5, -9]) == -1
    assert find_max([0]) == 0
