from tasks.task2_sum import sum_of_range

def test_sum_of_range():
    assert sum_of_range(1, 5) == 15
    assert sum_of_range(3, 7) == 25
    assert sum_of_range(0, 0) == 0
