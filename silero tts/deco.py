import time


def perform_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result =  func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__} took {end - start} seconds')
        return result
    return wrapper



@perform_time
def sum_two():
    time.sleep(1)
    return 1 + 1


print(sum_two())
