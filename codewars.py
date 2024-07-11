def open_or_senior(data):
    list = []
    for row in data:
        if row[0] >= 55 and row[1] > 7:
            list.append('Senior')
        else:
            list.append('Open')
    return list


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

def find_outlier(integers):
    ones_counter = 0
    list = [1 if is_even(integer) else 0 for integer in integers]
    if list.count(1) > 1:
        for integer in integers:
            if not is_even(integer):
                return integer
    else:
        for integer in integers:
            if is_even(integer):
                return integer


def to_hex(num):
    if 16 > num > 0:
        return "0"+hex(num)[2:].upper()
    elif num <= 0:
        return "00"
    elif num > 255:
        return "FF"
    else:
        return hex(num)[2:].upper()

def rgb(r, g, b):
    return to_hex(r) + to_hex(g) + to_hex(b)

def pig_it(text):
    words_list = list(text.split(" "))
    new_str = ''
    for word in words_list:
        if word not in "~!@#$%^&*()_+!№;%:?,.<>{}[]|/":
            word = word[1:] + word[0] + "ay"
            new_str += word + ' '
        else:
            new_str += word + ' '
    return new_str[:len(new_str)-1]

def is_needed(num):
    if num % 18 == 0:
         a = int(str(num)[0])
         b = int(str(num)[1])
         c = int(str(num)[2])
         d = int(str(num)[3])
         e = a * b * c * d
         if 0 < e < 12:
             return True

def func():
    for i in range(1000, 10000):
        if is_needed(i):
            print(i)

def squares(n):
    return sum([x**2 for x in range(1, n+1)])

def summa(array):
    return sum(array)

print([1,2,3,4,5,6,7,8,9,10])