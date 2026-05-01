from concurrent.futures import ThreadPoolExecutor
import time
import random

def do_task():
    print("Doing task...")
    random_sleep = random.random(1,5)
    time.sleep(random_sleep)
    print(f"Sleeping for {random_sleep} seconds")


# with ThreadPoolExecutor(max_workers=10) as executor:
#     executor.submit(do_task)


def square(x):
    return x * x

nums = [5, 10, 15]
mapped_nums = map(square, nums)
print(list(mapped_nums))
