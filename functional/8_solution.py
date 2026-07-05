#kwargs stands for keyword arguments.
#**kwargs allows a function to accept any number of named arguments.
#Inside the function, kwargs is stored as a dictionary.
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name="shaktiman", power="lazer")
print_kwargs(name="shaktiman")
print_kwargs(name="shaktiman", power="lazer", enemy = "Dr. Jackaal")