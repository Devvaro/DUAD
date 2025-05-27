from datetime import date

class User:
    date_of_birth: date

    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):

        today = date.today()
        return (
        today.year
        - self.date_of_birth.year
        - (
            (today.month, today.day)
        < (self.date_of_birth.month, self.date_of_birth.day)
            )
        )

def user_adult(func):
    def wrapper(user, *args):
        if user.age < 18:
            raise ValueError(f"The user is not over 18 years old")
        return func(user, *args)
    return wrapper


@user_adult
def check_user(user):
    print(f"Age: {my_user.age}")
    print("The user is an adult")

try:
    my_user= User(date(2008,9,8))
    check_user(my_user)
    
except ValueError as e:
    print(e)