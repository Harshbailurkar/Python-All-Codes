def greet(fx):
    def mfx( * args, **kwargs):
        print("good morning")
        fx(* args, **kwargs) # hello()
        print("tnx for using this function")
    return mfx

@greet
def hello():
    print("hello")

#     #or
# greet(hello)()

@greet
def add(a,b):
    print (a+b)
    #or
# greet(add)(5,10)
hello() 
print("------------------------------------------------------------------------------------------")
add(5,10)

print("------------------------------------------------------------------------------------------")

import logging

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b

my_function(5,10)