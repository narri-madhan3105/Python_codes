#difference btwn args and kwargs output
def demo(*args, **kwargs):
    print(args) #tuples
    print(kwargs) #dictionary

demo(1, 2, 3, name="Madhan", college="BIT")
#A normal function can take multiple inputs, but the number of inputs is fixed unless you use *args or **kwargs.