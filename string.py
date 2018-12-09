# string formatting

# name = 'Thanh Nhat Dao'
# age = 99.9
# print('My name is ' + name)
# print('He has ' + str(age) + " name age")

# print('My name is {name} and has {age}' .format(name=name, age=int(age)))

# F-String (3.6+)

# print(f"a this is {name} aa {int(age)}")


# print('Name is {name} and age is {age}'.format(name=name, age=age))

# String METHOD
# s = 'Hello PythonLl'
# title = 'this is main title'
# sub = 'h'
# print(s.count(sub.lower()))

# print(s.startswith(sub))

# ucfirst on_python
# print(title.title())

# a = 'abc'
# b = a.replace('a', 'f')
# print(b) ## fbc

# a = b"abc"
# b = a.replace(b"a", b"f")
# print(b)
s = 'helloworld1'
print(s.isalnum())
#============================= from github

# String Methods

s = 'helloworld'

# Capitalize string
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into a list
print(s.split())

# Find position
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())


