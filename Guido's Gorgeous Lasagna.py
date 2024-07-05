"""
:const EXPECTED_BAKE_TIME: int - total bake time for completed lasagna
"""

EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    
    """Calculate the preparation time in minutes.

    :param number_of_layers: int - baking time already elapsed.
    :return: int - preparation time (in minutes) derived from 'number_of_layers'.

    Function that takes the number of layers the lasagna has as an argument
    and returns how long it will take to prepare. 
    """
    return number_of_layers * 2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):

    """Calculate the elapsed time in minutes.

    :param elapsed_bake_time: int - baking time already elapsed.
    :param number_of_layers: int - number of layers of lasagna.
    :return: int - elapsed bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven and the number of layers
    as an argument and returns how many minutes the lasagna has been in the oven.
    """

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
