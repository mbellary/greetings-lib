from greetings_lib.greetings import greet

def test_greet_returns_correct_message():
    assert greet("World") == "Hello from World!"
