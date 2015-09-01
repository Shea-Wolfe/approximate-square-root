def number():
    try:
        user_num = float(input("Please enter a positive number."))
        if user_num < 0:
            print("That's not a positive number!")
            number()
        else:
            return user_num
    except:
        print('that\'s not a number at all!')
        number()
user_num = number()
y = 1
x = user_num
counter = 0
while round(y, 3) != round((y+(x/y))/2, 3):
    counter += 1
    y = (y+(x/y))/2
    print("this is attempt number " + str(counter) + " and the current guess is " + str(y))
print("the square root is " + str(y) + " and it took me " + str(counter) + " attempts!")
