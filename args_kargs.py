# *args    = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
# * unpacking operator
# when using the *args, the arguments are turned into a tuple
from openpyxl.styles.builtins import total


def add(*args):
    total = 0
    for arg in args:
        total+= arg
    return total

print(add(1,2,3,4,5,6))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

# display_name("Dr.", "Spongebob", "Squarepants")

def address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} - {value}")

address(street= "123 Fake Street",
        city="Detroit",
        state="Michigan",
        zip="12312")

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('apt')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')}")

shipping_label("Dr.", "Spongebob", "Squarepants", "III",
               street= "4444 Square",
               apt= "Square",
               city="Bikins Rift",
               state="Ocean",
               zip="123123",)


def sum(*args):
    total = 0
    for arg in args:
        total+=arg
    return total

print(sum(1,2,3,4))

def show_user(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")

show_user(name="spongebob",
          age=12,
          type="square")

def desc_order(*args, **kwargs):
    for arg in args:
        print(f"Item: {arg}")

    print("Description: ")
    for key,value in kwargs.items():
        print(f"{key}: {value}" )

desc_order("Tomate",
           seeds= False,
           type="Italian",
           stage="Maduro")

def choose_items(*args, **kwargs):
    for arg in args:
        print(arg)

    for key, value in kwargs.items():
        if "categoria" not in kwargs.keys():
            print("There is no field *categoria*")
            break
        else:
            print(f"{key}: {value}")


choose_items("G403", categoria= "Eletronico",
             preco=333.3,
             marca="Logitech")

choose_items("Vivobook",
             preco=888.8,
             marca="Asus")