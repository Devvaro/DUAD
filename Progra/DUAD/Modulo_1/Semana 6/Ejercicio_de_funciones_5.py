def look_for_upper_and_lower(string):
    upper_case = 0
    lower_case=0


    for char in string :
        if char.isupper():
            upper_case += 1
        elif char.islower():
            lower_case += 1


    print(f"There's {upper_case} upper cases and {lower_case} lower cases")


look_for_upper_and_lower("I lover KFC")

