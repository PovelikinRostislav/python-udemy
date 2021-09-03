def func_to_wrap(arg):
    print(f"That's the function to wrap with an arg {arg}")

def wrap(func):
    def new_function():
        constant_argument = 42
        func(42)
        print("That's the new function msg after func was executed")
    return new_function

@wrap
def func_to_decorate(arg):
    print(f"That's the function to decorate with an arg {arg}")

def main():
    func_to_wrap(5)
    wrapped_function = wrap(func_to_wrap)
    wrapped_function()
    # Next call shows the main diff between decorator and decorator-like impl
    # Decorator-like implementation doesn't substitute the previous func definition
    # (unless you rebind the function name to the same one)
    func_to_wrap(13)

    print("=====")
    func_to_decorate()

if __name__ == "__main__":
    main()
