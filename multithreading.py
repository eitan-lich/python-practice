from concurrent.futures import ThreadPoolExecutor
import time
import random

def do_task(num):
    print("Doing task...")
    random_sleep = random.randint(1,5)
    time.sleep(random_sleep)
    print(f"Sleeping for {random_sleep} seconds")

with ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(do_task, range(5)))

print(results)