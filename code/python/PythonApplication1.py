def NameFunction():
    name = input("What is your name? ")
    print("Aloha mahalo " + name)
    return name

def Sum_func():
    print("Just Testing")

    x = input("First: ")
    y = input("Second: ")

    sum = float(x) + float(y)
    print("Sum: " + str(sum))

def Weight_func():

    weight = int(input("Weight: "))
    unit_option = input("(K)g or (L)bs:")

    if unit_option.upper() == "K":
        converted_value = weight / 0.45
        print("Weight in Lbs:" + str(converted_value))
    else:
        converted_value = weight * 0.45
        print("Weight in Kg:" + str(converted_value))


NameFunction(); print("")
Sum_func(); print("")

birth_year = input("Enter your birth year: ")
age = 2020 - int(birth_year)
print(age)


course = 'Python for Beginners'
print(course.upper())
print(course.find('for'))
print(course.replace('for', '4'))
print('Python' in course) #True


print(10 / 3)   # 3.3333333333333335
print(10 // 3)  # 3
print(10 % 3)   # 1
print(10 ** 3)  # 1000
print(10 * 3)   # 30


x = 10
x = x + 3
x += 3

x = 10 + 3 * 2


temperature = 35

if temperature > 30:
    print("Hot night, in a cold town")
    print("Drink infinite water")
elif temperature > 20:
    print("It's a fine day")
elif temperature > 10:
    print("It's a bit cold")
else:
    print("It's cold")
    print("LORT! ~ Snehaderen")


Weight_func(); print("")



i = 1
while i <= 1_1:
    #print(i)
    print(i * '*')
    i += 1

names = ["Doktor Derp", "Jens Jensen", "John Smith", "Toni Bonde", "James Bond", "Isaac Clark", "DOOMGUY"]
print(names)
print(names[0])
print(names[-1]) # Last Element - DOOMGUY
print(names[0:3]) # ['Doktor Derp', 'Jens Jensen', 'John Smith']


numbers = [1,2,3,4,5]
numbers.append(6)
numbers.insert(0,-1)
numbers.remove(3)
#numbers.clear()

print(numbers)
print(1 in numbers)
print(len(numbers))


for item in numbers:
    print(item)

i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1


#range_numbers = range(5)
#range_numbers = range(5, 10)
range_numbers = range(5, 10, 2)
print(range_numbers)

for number in range_numbers:
    print(number)

for number in range(7,45,5):
    print(number)

numbers2 = (1,2,3) #Tuple