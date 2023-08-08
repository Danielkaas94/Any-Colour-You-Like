''' ##########################################################################

        _____       _   _                    _  __     _          ______ 
        |  __ \     | | | |                  | |/ /    | |        |____  |
        | |__) |   _| |_| |__   ___  _ __    | ' / __ _| |_ __ _      / / 
        |  ___/ | | | __| '_ \ / _ \| '_ \   |  < / _` | __/ _` |    / /  
        | |   | |_| | |_| | | | (_) | | | |  | . \ (_| | || (_| |   / /   
        |_|    \__, |\__|_| |_|\___/|_| |_|  |_|\_\__,_|\__\__,_|  /_/    
                __/ |                                                     
                |___/                                                      
        
''' ##########################################################################

def square_digits(num):
    """
    Squares each digit of the given number and concatenates the results.
    
    Args:
        num (int): The input number to be processed.
        
    Returns:
        int: The resulting number after squaring and concatenating the digits.
    """

    # Convert the number to a string to work with individual digits
    num_str = str(num)
    
    # Initialize an empty string to store the concatenated squared digits
    result_str = ""
    
    # Iterate through each digit in the string
    for digit in num_str:
        # Convert the digit back to an integer, square it, and convert it back to a string
        squared_digit = str(int(digit) ** 2)
        
        # Append the squared digit to the result string
        result_str += squared_digit
    
    # Convert the concatenated squared digits back to an integer and return it
    return int(result_str)


def square_digits2(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)

def square_digits3(num):
    return int(''.join(str(int(d)**2) for d in str(num)))


def square_digits4(num):
    # s converts num to a str so we can index through it
    # when then loop through the len of the str 
    # while we're looping the string we convert it back to a int and square it
    # after we add it to a str to keep it from adding and then convert it to a int
    s = str(num)
    t = len(s)
    y=0
    g= 0
    b=""
    while y < t:
        g = int(s[y])**2 
        b= b+ str(g) 
        final = int(b)
        y=y+1
    return(final)   
    pass



# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| #