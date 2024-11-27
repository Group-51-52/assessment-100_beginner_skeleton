from tasks.task3_vowels import count_vowels

def test_count_vowels():
    assert count_vowels("Programming") == 3
    assert count_vowels("AEIOU") == 5
    assert count_vowels("xyz") == 0
