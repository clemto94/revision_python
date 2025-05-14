import time

def repeat(num_repeat: int, with_error: bool = False, error=Exception):
    def decorator(func):
        def wrapper(*args, **kwargs):
            value = 0
            for i in range(num_repeat):
                try:
                    value = func(*args, **kwargs)
                except error as e:
                    print("Error caught")
                    if with_error:
                        raise e
                    continue
            return value
        return wrapper
    return decorator

@repeat(2, error=ZeroDivisionError)
def divide(dividend, divisor):
    print("Call function divide")
    return dividend / divisor

### timer decorator
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        return (result, end-start)
    return wrapper

@timer
def my_func(i: int):
    time.sleep(i)
    return (i + i, i * i)

for i in range(6):
    print(my_func(i))

if __name__ == '__main__':
    result = divide(20, 0)
    print(result)
