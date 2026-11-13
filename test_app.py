from app import greet

def test_greet():
    assert greet("Abhishek") == "Hello, Abhishek! This is an automated CI/cd deployment."

def test_greet_student():
    assert greet("student") == "Hello, student! This is an automated CI/cd deployment."
