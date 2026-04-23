from functools import wraps
import time


def security_level(n):
    def change_case(func):
        @wraps(func)  # This preserves the original name (security)
        def inner(x):
            if n <= 0:
                return func(x)
            else:
                return func(x).upper()

        return inner

    return change_case


@security_level(1)
def security(name):
    return "security: " + name


print(f"DEBUG: {security.__name__}")
print(security("novisio"))


# Repeats the function n times


def repeater(n):
    def repeat_function(func):
        @wraps(func)
        def inner():
            for i in range(n):
                func()

        return inner

    return repeat_function


@repeater(10)
def greet():
    print("Hello")


greet()

# Limits the amount a function can be called


def limiter(n):
    def limit_count(func):
        count = 0

        def inner():
            nonlocal count
            if count < n:
                count += 1
                func()
            else:
                print("Limit reached.")

        return inner

    return limit_count


@limiter(3)
def goodbye():
    print("Good bye!")


goodbye()

# Logs what the function does.


def debug_logger(func):
    @wraps(func)
    def inner(*args, **kwargs):
        func_name = func.__name__
        func_result = func(*args, **kwargs)
        print(f"Calling function: {func_name} with args: {args}, and kwargs: {kwargs}")
        print(f"{func_name} returned: {func_result}")
        return func_result

    return inner


@debug_logger
def add(a, b):
    return a + b


result = add(10, 20)
print(f"The final result is {result}")


def measure_time(func):
    @wraps(func)
    def inner(*args, **kwargs):
        function_name = func.__name__
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(
            f"[TIMER]: {function_name} took [{-start_time + end_time}] seconds to execute."
        )
        return result

    return inner


@measure_time
def simple_function():
    time.sleep(2)
    print("hi there.")


simple_function()
