## 2. Hello World
print('hello world')

## 3. Variables and data types

bool = True
integer = 1
floating_point = 2.0
string = "My String"

my_tuple = (1, 2, 3)
print(my_tuple[0])  # index starts at 0
print(my_tuple[1])
print(my_tuple[2])


my_list = [1, 2, 3]
print(my_list[0])  # index starts at 0
print(my_list[1])
print(my_list[2])

my_range_0_9 = range(10)  # 0-9, 10 is excluded
my_range_5_9 = range(5, 10)  # 5-9, 10 is excluded

my_dictionary = {
    'name': "Geyer",
    'age': 28
}

print(f"Name: {my_dictionary['name']}")
print(f"Age: {my_dictionary.get('age')}")
print(f"Age: {my_dictionary.get('surname')}")
print(f"Age: {my_dictionary.get('surname', 'No Surname')}")

months = {
    1: "Jan",
    2: "Feb"
}


## Strings
phase = "Python is Fun"
print(phase.upper())
print(phase.lower())

print(phase.isupper())
print(phase.upper().isupper())

print(len(phase))
print(phase[0])
print(phase[1])

for character in phase:
    print(character.upper())

## Numbers

print(4 * -3 + 5 / 2)  # +, -, *, /, **
print((4 * -3) + (5 / 2))
print(10 % 3)  # modulus gives remainder
print(10 // 3)  # integer division
print(abs(-5))
print(max(1, 2, 3, 4))  # max, min
print(round(3.5))

# There are many more math functions in the math library


## Lists

numbers = [1, 2, 3 , 4, 5]
names = ["Kevin", "Karin", "Jim", "Oscar", "Toby"]
print(names)
print(names[0])
print(names[1])
print(names[-1])
print(names[1:3])  # from 1 to 3, excluding 3
print(names[1:])  # from 1 onward
names[1] = "Mike"
print(names)

print(names.extend(numbers))
print(names.append("Jason"))
print(names.insert(1, "Kelly"))
print(names.remove("Jim"))
print(names.clear())
print(names.pop())  # remove last element
print(names.count("Jim"))
print(names.sort())
print(names.reverse())
print("Mike" in names)

copy_names = names.copy()
print(copy_names)

## Tuples
# Like lists, but with restrictions
# cannot be edited after it has been created (immutable)
# use for data that will not change

coordinates = (4, 5)
coordinates[1] = 2  # will give an error
print(coordinates[0])

#create a list of tuples
coordinates = [(4, 5), (4, 5), (4, 5)]


## Functions
# indentation matters

def percentage_diff(number_1, number_2):
    result = (number_1 - number_2) / number_2
    return result

print(percentage_diff(3, 2))

# Importing functions that you have written from other files
from useful_tools import roll_dice, file_extension
roll_dice(6)
file_extension("master_data.csv")

# 4. Importing



