from multipledispatch import dispatch
@dispatch(int, int)
def add(num1, num2):
    print(num1 + num2)

@dispatch(int, int, int) 
def add(num1, num2, num3):
    print(num1 + num2 + num3)


# Calls the first function
add(3, 4)

# Calls the second function
add(3, 4, 1)
