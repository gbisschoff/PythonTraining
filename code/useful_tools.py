"""
Some useful tools written as part of the example code
"""
from random import randint


def roll_dice(num):
    """
    Simulate rolling a dice with 'num' sides
    :param num: the number of sides to the dice
    :return: a random number between 1 and 'num'
    """
    return randint(1, num)


def file_extension(filename):
    """
    Get the file extension of a file
    :param filename: a file name or path
    :return: the file extension
    """
    return filename[filename.index(".") + 1:]
