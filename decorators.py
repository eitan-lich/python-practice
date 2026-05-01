def first_layer(times):
    def second_layer(func):
        def actual_func(*args, **kwargs):
            print(f"Content add {times} times before real function call")
            func(*args, **kwargs)
            print(f"Content add {times} times after real function call")
        return actual_func
    return second_layer



@first_layer(times=3)
def my_func(custom_message, custom_val=""):
    print(f"my_func actual print {custom_message} because custom {custom_val}")

my_func("test me", custom_val="Potentially")