# python oop

# creating classes

class Friends:

    gender = 'male'                 # class variables
    num_of_friends = 0
    raise_age = 2

    def __init__(self, name, hobby, age):         
        self.name = name                      # instance variables(everything with 'self' in it)
        self.hobby = hobby
        self.age = age

        Friends.num_of_friends += 1

    def intro(self):                  # instance methods
        print(f"My name is, {self.name}. I am {self.age} years old. I am {self.gender}")

    def age_plus(self):
        self.age = self.age + self.raise_age

    def sex_chng(self):
        self.gender = "female"

    @classmethod                        # class methods. it takes 'cls' instead of 'self'
    def chng_raise_age(cls, extension):
        cls.raise_age = extension

    @classmethod
    def from_string(cls, frnd_str):
        name, hobby, age = frnd_str.split("-")
        return cls(name, hobby, age)
    
    @staticmethod                       #static method. used when we not using instance or cls
    def is_partyday(day):
        if day ==  6 or day == 5:
            return "Party time"
        else:
            return "Go study!"

eric = Friends("Eric", "coding", 26)
siina = Friends("Siina", "dancing", 27)

new_friend = "Jaakko-drinking-25"
Jaakko = Friends.from_string(new_friend)

import datetime
my_date = datetime.date(2024, 2, 14)

print(Friends.is_partyday(my_date))
