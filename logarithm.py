import math

def logarithm(number, base):
    if(number > 0 and base > 1) :
        return math.log(number, base)
    return "The input number shall be greater than zero and base shall be greater than 1"


