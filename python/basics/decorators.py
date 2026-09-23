#Decorators
import logging

from functools import wraps

logging.basicConfig(level = logging.INFO, filename = "exercise5.log", filemode = "w")
logger = logging.getLogger(__name__)

def log_execution(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        
        result = func(*args,**kwargs)
        logger.info(f"calling  {func.__name__} returned {result}")
        
        return result
    return wrap

@log_execution
def get_status():
    return "OK"

@log_execution
def add(a,b):
    """Add two numbers."""
    return a+b

@log_execution
def greet(name, age):
    return f"{name} is {age} years old"

@log_execution
def create_user(name, email, is_active=True):
    return {
        "name": name,
        "email": email,
        "is_active": is_active
    }

@log_execution
def divide(a, b):
    return a / b

print(add.__name__)
print(add.__doc__)
print(add(10, 20))

greet("Saiam", 21)

create_user(
    name="Saiam",
    email="saiam@example.com",
    is_active=True
)

print(get_status())

divide(10, 2)
# divide(10, 0)