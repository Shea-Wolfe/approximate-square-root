def number():
    """Takes user input and checks to make sure it is a positive number.
    takes no arguements"""
    try:
        user_num = float(input("Please enter a number."))
        if user_num < 0:
            return (abs(user_num), "i")
        else:
            return (user_num, 1)
    except:
        print('that\'s not a number at all!')
        number()
user_num = number()
y = 1
x, z = user_num
counter = 0
while round(y, 3) != round((y+(x/y))/2, 3):
    counter += 1
    y = (y+(x/y))/2
    print("this is attempt number " + str(counter) + " and the current guess is " + str(y))
print("the square root is " + str(y) + "*" + z + " and it took me " + str(counter) + " attempts!")
