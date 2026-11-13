def greet(name):
    return f"Hello, {name}! This is an automated CI/cd deployment."


def welcome():
    return "Welcome to the Feature Branch!"


if __name__ == "__main__":
    print(greet("Student"))
    print(welcome())
