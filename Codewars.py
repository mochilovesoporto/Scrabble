def check_two_characters(var1, var2):
    if type(var1) and type(var2) != str:
        return -1
    elif var1.isupper() and var2.isupper() == True:
        return 1
    elif var1.islower() and var2.islower() == True:
        return 1
    else:
        return 0

print(check_two_characters(0, ?))
