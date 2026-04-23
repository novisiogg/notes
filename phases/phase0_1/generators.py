import math
file_simulator = {
    

    "i dont know what i am doing, this is just an example i dont know what i am doing, this is just an example i dont know what i am doing, this is just an example "
}


def get_log_lines_list():
    for char in file_simulator:
        return char


def stream_log_lines():
    for char in file_simulator:
        yield char


print(get_log_lines_list())
for char in stream_log_lines():
    print(char)

# Generators
class OddNumbers():
    def __iter__(self):
        self.n = 1
        return self
    
    def __next__(self):
        self.n+=2
        result = self.n
        return result

odd = OddNumbers()
it = iter(odd)
# Returns odd numbers starting from 1 til X
for i, n in enumerate(range(1,19)):
    print(f"{i+1} number: {next(it)}")
    
# [expression for item in iterable if condition] - List comprehensions
names_list = ["novisiogg", "zouma", "tyx", "regedit"]
# removes name if it's not "novisiogg"
res = [names_list.remove(name) for name in reversed(names_list) if name != "novisiogg"] # reversed since we're updating the list in a loop
print(names_list)

# {key_expression: value_expression for item in iterable if condition} - Dictionary comprehension
# Returns the square root of a number from x to y-1
result = {num: math.sqrt(num) for num in range(1,10)}
print(result)


first_names = ["novisio", "zouma", "tyx"]
last_names = ["gg", "games", "maftouh"]

another_result = {a: b for a, b in zip(first_names, last_names)}
print(another_result)

# {expression for item in iterable if condition} - Set comprehensions (same as List)

l = [1, 1, 3, 2, 5, 6]
reslt = {num**2 for num in l}
print(reslt)



