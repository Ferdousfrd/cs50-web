#learning about decorators
#decorators are used to modify a function with another function

def announcement(f):
    def wrapper():
        print("Hellooo, welcome!")
        f()
        print("Byeee")
    return wrapper

@announcement
def hello():
    print("name stuff")

hello()