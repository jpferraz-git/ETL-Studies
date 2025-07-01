
def creatingLists():
    fruit_list = ["apple", "banana", "orange", "coconut", 10, 15.50]
    print(f"Full_list: {fruit_list}")
    print(f"Accessing a index od the List: {fruit_list[0]}")
    print(f"Accessing the indexes in the range of 1 to 3: {fruit_list[1:3]}")
    print(f"Accessing the indexes in by 2 for 2: {fruit_list[::2]}")
    print(f"Accessing the indexes in by 2 for 2, starting in the index 2: {fruit_list[2:2]}")
    print(f"Accessing the indexes in inverted order of the List: {fruit_list[::-1]}")

    print(list(map(lambda f: f, fruit_list)))
    print(f"Acessing the length of a list: {len(fruit_list)}")
    print(f"Checking if a value exist in the list: {'banana' in fruit_list}")

    fruit_list.append("strawberry") #Adds a value to the end of the list
    fruit_list.remove("apple") #Removes a value of the list
    fruit_list.insert(0, "potato") #Adds a value to an specific index

def creatingSets():
    cars = {"civic", "celta", "uno", "911"}
    frozen_cars = (["civic", "celta", "gol"])

    focus = "focus"
    cars.add(focus)

    more_cars = ("siena", "gol")

    remove_cars = ("civic", "uno")

    for i in range(len(more_cars)):
        cars.add(more_cars[i])
        cars.remove(remove_cars[i])

    remove_civic = lambda:'civic' in cars and cars.remove('civic')

    remove_civic()
    print(cars)

def creatingTuples():
    birthDates = ("12/12/12", "03/04/05", "25/12/04", "08/04/32")

    cars_brad = {
        "Honda": "Civic",
        "Fiat": "Uno",
        "Byd": "Byd",
        "Honda": "911"
    }


# creatingLists()
creatingSets()