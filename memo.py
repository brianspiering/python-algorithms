from functools import wraps

def memo(func):
    """A function that stores cached values from other functions.
    Can be used as a decorator to avoid rewriting a function as a generator.

    From Python Algorithms by Magnus Lie Hetland.
    """
    cache = {}                          # Stored subproblem solutions
    @wraps(func)                        # Make wrap look like func
    def wrap(*args):                    # The memoized wrapper
        if args not in cache:           # Not already computed?
            cache[args] = func(*args)   # Compute & cache the solution
        return cache[args]              # Return the cached solution
    return wrap                         # Return the wrapper