#Python has no command for declaring a variable. A variable is created the moment you first assign a value to it.

x = 5
y = "Lewo"
print(x)
print(y)

#Variables do not need to be declared with any particular type, and can even change type after they have been set.

x = 4       # x is of type int
x = "Lewo" # x is now of type str
print(x)

#If you want to specify the data type of a variable, this can be done with casting.

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#You can get the data type of a variable with the type() function.

x = 5
y = "Lewo"
print(type(x))
print(type(y))

#String variables can be declared either by using single or double quotes:

x = "Lewo"
# is the same as
x = 'Lewo'

#Variable names are case-sensitive.

a = 4
A = "Lewo"
#A will not overwrite a