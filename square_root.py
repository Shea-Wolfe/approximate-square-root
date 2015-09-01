def number():
    try:
        user_num = int(input("Please enter a positive number."))
        if user_num < 0:
            print("That's not a positive number!")
            number()
        else:
            return user_num
    except:
        print('that\'s not a number at all!')
        number()
