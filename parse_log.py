from collections import defaultdict
import random
import time
# error_logs = {}
error_logs = defaultdict(int)

with open("23_12_3_run.log") as log_file:
    for line in log_file:
        if "ERROR" in line:
            error_content = line.split("-")[4].strip()
            error_logs[error_content] += 1
            # error_logs[error_content] = error_logs.get(error_content,0) + 1

print(list(error_logs))

def add_val(val, li=[]):
    li.append(val)
    return li

print(add_val(20))
print(add_val(50))
print(add_val(70))


print([random.randint(0,5) for _ in range(10)])

start_gen = time.time()
random_gen = (random.randint(50,10000000)**random.randint(50,10000000) for _ in range(10000000000))
end_gen = time.time()
print(f"It took the generations {end_gen - start_gen} seconds to create")

start_list = time.time()
random_list = [random.randint(50,1000)**random.randint(50,1000) for _ in range(100)]
end_list = time.time()
print(f"It took the generations {end_list - start_list} seconds to create")
