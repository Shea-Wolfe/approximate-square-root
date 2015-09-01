def number():
    """Takes user input and checks to make sure it is a positive number.
    takes no arguements"""
    try:
        user_num = float(input("Please enter a number."))
        if user_num < 0: #
            return (abs(user_num), "i") #i is used here to represent sqrt(-1) it's not operable but it'd tell a human what's happening
        else:
            return (user_num, 1) #the 1 here is to prevent an error when we unpack below it looks funny but it's still correct
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
print("the square root is " + str(y) + "*" + str(z) + " and it took me " + str(counter) + " attempts!")
