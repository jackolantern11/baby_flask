import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        return_value = func(*args, **kwargs)
        print(f"Function: {func.__name__} Run Time: {time.time() - start_time}s")
        return return_value

    return wrapper
