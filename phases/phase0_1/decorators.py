from functools import wraps


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

from functools import wraps


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
