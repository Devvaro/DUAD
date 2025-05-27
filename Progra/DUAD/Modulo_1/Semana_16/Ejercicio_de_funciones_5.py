def look_for_upper_and_lower(string):
    upper_case = 0
    lower_case=0


    for char in string :
        if char.isupper():
            upper_case += 1
        elif char.islower():
            lower_case += 1


    return upper_case, lower_case
    

print(look_for_upper_and_lower("I love KFC")) # (3, 5)





