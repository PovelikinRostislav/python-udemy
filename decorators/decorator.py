def func_to_wrap(arg):
    print(f"That's the function to wrap with an arg {arg}")

def wrap(func):
    def new_function():
        constant_argument = 42
        func(42)
        print("That's the new function msg after func was executed")
    return new_function

def main():
    func_to_wrap(5)
    wrapped_function = wrap(func_to_wrap)
    wrapped_function()
    func_to_wrap(13)

if __name__ == "__main__":
    main()
