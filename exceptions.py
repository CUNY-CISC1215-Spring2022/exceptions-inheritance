def factorial(n):
    """
        Compute the factorial of an integer in
    """

    # If n is not an integer, we probably can't compute a factorial.
    # Catch the issue with a guardian pattern and raise an exception.
    if not isinstance(n, int):
        raise TypeError("Factorial must be called with integer value")
    if n == 0: # Base case: If n is 0, return immediately
        return 1

    # Recursive case: Compute the factorial
    return n * factorial(n-1)

# Compute factorial for all these numbers:
a = [1, 2, 3, 4, 5.2, 6, 7]

for val in a:
    # Put the factorial() call in a try block in case it raises an exception
    try:
        print(factorial(val))
    except:
        # Uh oh, it raised an exception - don't let it crash the program.
        # Just print out information about the bad number, and keep going
        # through the list.
        print(f"Uh oh, we gave factorial() a bad value: {val}")