"""
The ancient Egyptians used to express fractions as sum of several terms where each numerator is one. For Example, 4/13
can be represented as 1/4+1/18+1/468. Create an algorithm to turn ordinary fraction a/b where a<b into an Egyptian fraction

"""
"""
pseudocode
1. find the largest unit fraction
2. remove it
3. for the remaining repeat 1 and 2
4. end when the final fraction is found
"""
import math
import fractions
from os import devnull


def solution(num,den):
        
    if (num<=0 or den<=0):
        return None

    elif (den%num==0):
        return int(den/num)
      
    else:
        
        unit = den//num+1
        return unit
            
def egyptian_decimal(num,den):
    unit = solution(num,den)
    if unit is None:
        return ""
    
    numerator = num*unit - den
    denominator = unit*den
    return f"+ 1/{unit} "+egyptian_decimal(numerator,denominator)
   


print(egyptian_decimal(4,13))

