def my_range(n):
    i = 0
    while i < n:
        yield i
        print("\t=> RESUME ITERATION AFTER YIELD")
        i += 1

def no_yield():
    if True:
        return 5
    else:
        yield 3

def main():
    my_range_generator = my_range(2)
    print(f"Generator-function is a function with yield expression inside:\n\t{my_range_generator}")

    not_yielding_generator = no_yield()
    print(f"Even if the generator function isn't going to reach yield expression at all, it will return a generator:\n\t{not_yielding_generator}")

    print("Each time you call generator function - it doesn't execute ANY code. It just creates a new generator to iterate over. (Pay attention to addresses)")
    for i in range(3):
        gen = no_yield()
        print(f"\t{gen}")

    print(f"But the type of the generator-function is always just function:\n\t{no_yield}")

    print(f"The generator is used as iterable object, cause it has __iter__ method which returns the iterator:\n\t{not_yielding_generator.__iter__}")
    print("The main idea of iteration over generator is that next() call on the generator's iterator will resume the execution after the previous yield expression until StopIteration raised")
    iterator = iter(my_range_generator)
    print(f"\tIterator of my_range_generator(2): {iterator}")
    value = next(iterator)
    print(f"\tFirst value of my_range_generator(2): {value}")
    value = next(iterator)
    print(f"\tSecond value of my_range_generator generator: {value}")
    try:
        next(iterator)
    except StopIteration as exception:
        print(f"\tException was caught on the 3rd next() call: {exception}")


    print("One of the biggest advantages of generators is that the memory footprint is very small.")
    print("Generator will issue one value at a time and consumer will be able to retrieve elements from it one-by-one")
    print("But important to notice that generator is one-way iterable. It has no rewind-like method")

    print("*******")
    print("Advanced and interesting part. There is no tuple-comprehensions in Python. Parenthesis usage is a generator comprehension!")
    my_list = [1,2,3,4,5]
    new_list = (elem for elem in my_list if elem > 3)
    print(f"Here it is, new generator:\n\t{new_list}")
    print(f"And the elements it's producing")
    for elem in new_list:
        print(f"\t\t{elem}")


if __name__ == "__main__":
    main()
