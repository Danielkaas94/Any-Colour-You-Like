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


def high(s):
    """
    Highest Scoring Word
    """
    def word_score(word):
        return sum(ord(c) - ord('a') + 1 for c in word)

    words = s.split()
    highest_score = 0
    highest_word = ""

    for word in words:
        score = word_score(word)
        if score > highest_score:
            highest_score = score
            highest_word = word

    return highest_word


def high2(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))


def high3(x):
    words=x.split(' ')
    list = []
    for i in words:
        scores = [sum([ord(char) - 96 for char in i])]
        list.append(scores)
    return words[list.index(max(list))]


def high4(x):
    scoreboard=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    heck = x.split()
    score=0
    score_final=0
    big_word=[]
    for each in heck:
        print(each)
        for every in each:
            if every in scoreboard:
                score= score + scoreboard.index(every) + 1
                print(score)
        if score > score_final:
            score_final = score
            big_word = each
            score = 0
        else:
            score = 0
    return big_word

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| #



# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| #
