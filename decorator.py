def hello():
    print("Hello, world!")

hello()
def decarator_example(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")
    return wrapper
@decarator_example
def hello():
    print("Hello")
hello()
