def sort_list(lst):
    if any(isinstance(item, int) for item in lst):
        raise ValueError("This function only works with strings")
    
    sorted_list = sorted(lst)
    return sorted_list

print(sort_list(["python","Function","variable","list","Action"]))

