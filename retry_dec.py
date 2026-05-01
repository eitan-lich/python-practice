from functools import wraps
import time

def retry(times=3,delay=10):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(times):
                print(f"The function {func.__name__} is going to be retried {times} time/s with a delay of {delay}s")
                print(f"Attempt {attempt+1}")
                result = func(*args, **kwargs)
                if result == 0:
                    print("Function executed successfully")
                    return
                print(f"Attempting again {attempt+1}/{times}")
                print(f"Pausing {delay}s before next attempt")
                time.sleep(delay)
        return wrapper
    return decorator

@retry()
def my_executor():
    return 3;

my_executor()