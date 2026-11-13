from app import greet

def test_greet():
	assert greet("Abhishek") == "Hello, Abhishek! Welcome to DevOps Lab."

def test_greet_student():
	assert greet("student") == "Hello, student! Welcome to DevOps Lab."

