from tasks.task1_greeting import generate_greeting

def test_generate_greeting():
    assert generate_greeting("Alice") == "Hello, Alice! Welcome to the coding world."
    assert generate_greeting("Bob") == "Hello, Bob! Welcome to the coding world."
    assert generate_greeting("") == "Hello, ! Welcome to the coding world."
