#Arihant Kunda
#June 16, 2021
#Idea for project taken from: https://www.youtube.com/watch?v=6tNS--WetLI

import d_roll 

def add(x, y):
    """add function"""
    return x + y

def subtract(x, y):
    """subtract function"""
    return x - y

def multiply(x, y):
    """multiply function"""
    return x * y

def devide(x, y):
    """devide function"""
    if y == 0:
        raise ValueError('Cannont Devide by 0!')
    return x / y

def dice_add(y):
    """adds dice roll with give number"""
    result = d_roll.roll_dice()
    return result + y
