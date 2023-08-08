''' ##########################################################################

        _____       _   _                    _  __     _            __  
        |  __ \     | | | |                  | |/ /    | |          / /  
        | |__) |   _| |_| |__   ___  _ __    | ' / __ _| |_ __ _   / /_  
        |  ___/ | | | __| '_ \ / _ \| '_ \   |  < / _` | __/ _` | | '_ \ 
        | |   | |_| | |_| | | | (_) | | | |  | . \ (_| | || (_| | | (_) |
        |_|    \__, |\__|_| |_|\___/|_| |_|  |_|\_\__,_|\__\__,_|  \___/ 
                __/ |                                                    
               |___/                                                                                                                                                      
        
''' ##########################################################################


'''



'''
def persistence(num):
    """
    Takes in a positive parameter num and returns its multiplicative persistence, 
    which is the number of times you must multiply the digits in num until you reach a single digit.
    """

    if num < 10:
        return 0
    
    persistence_count = 0
    
    while num >= 10:
        product = 1
        while num > 0:
            product *= num % 10
            num //= 10
        num = product
        persistence_count += 1
    
    return persistence_count



import operator
def persistence2(n):
    i = 0
    while n>=10:
        n=reduce(operator.mul,[int(x) for x in str(n)],1)
        i+=1
    return i

def persistence3(n):
    n = str(n)
    count = 0
    while len(n) > 1:
        p = 1
        for i in n:
            p *= int(i)
        n = str(p)
        count += 1
    return count

def persistence4(n):
    nums = [int(x) for x in str(n)]
    sist = 0
    while len(nums) > 1:
        newNum = reduce(lambda x, y: x * y, nums)
        nums = [int(x) for x in str(newNum)]
        sist = sist + 1
    return sist

from operator import mul
def persistence5(n):
    return 0 if n<10 else persistence(reduce(mul,[int(i) for i in str(n)],1))+1




# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| #



# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| #



# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| #
