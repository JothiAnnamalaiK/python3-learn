# decorator is a func that takes a func, it creates neew func inside its body (wrapper). then it returns that new function


def my_decorator(func):
    def wrapper():
        print("I am abt to execute the func...")
        func()
        print("I have executed the func..")

    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


say_hello()
