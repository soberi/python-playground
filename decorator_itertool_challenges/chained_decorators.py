# Make a chain of function decorators.

from datetime import datetime

# Decorator example
def not_during_the_night(func):
    """Function only runs during the day."""
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass
    return wrapper
    
def good_day():
    print("Good day to you!")

good_day = not_during_the_night(good_day)


# Using pie syntax with @
def quiet_night(func):
    def wrapper_quiet_night():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass
    return wrapper_quiet_night

@quiet_night # shortened good_day_again = quiet_time(good_day_again)
def good_day_again():
    print("Good day again to you")


# Chained decorator: inner, mid, outer

def outer_world(func):
    def wrapper_outer_world(*args, **kwargs):
        print("We need a rocket.")
        return func(*args, **kwargs)
    return wrapper_outer_world

def mid_world(func):
    def wrapper_mid_world(*args, **kwargs):
        print("We need a plane.")
        return func(*args, **kwargs)
    return wrapper_mid_world

@outer_world
@mid_world
def inner_world():
    print("We need a car.")

